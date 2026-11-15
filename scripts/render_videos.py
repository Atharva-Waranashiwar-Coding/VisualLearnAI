#!/usr/bin/env python3
"""Render vertical narrated educational MP4s from validated JSON using Pillow, espeak-ng and ffmpeg."""
import argparse,json,math,os,subprocess,tempfile,textwrap
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
def font(size):
 for path in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf']:
  if Path(path).exists():return ImageFont.truetype(path,size)
 return ImageFont.load_default()
def wrap(draw,text,ft,width):
 words=text.split();lines=[];line=''
 for word in words:
  nxt=(line+' '+word).strip()
  if draw.textbbox((0,0),nxt,font=ft)[2]>width and line:lines.append(line);line=word
  else:line=nxt
 if line:lines.append(line)
 return lines
def frame(item,t,duration):
 im=Image.new('RGB',(540,960),(10,19,36));d=ImageDraw.Draw(im)
 for r in range(390,20,-12):
  shade=int(25+(390-r)/40);d.ellipse((270-r,350-r,270+r,350+r),outline=(15,shade+25,shade+38),width=2)
 d.text((270,155),'VISUALLEARN AI',font=font(22),fill='#9ef2ce',anchor='mm')
 for j,line in enumerate(wrap(d,item['title'],font(29),480)[:2]):d.text((270,225+j*38),line,font=font(29),fill='white',anchor='mm')
 for i,node in enumerate(item['nodes']):
  y=338+i*126;active=(int(t*1.4)%3==i)
  d.rounded_rectangle((65,y,475,y+82),radius=18,fill='#26665b' if active else '#1d3049',outline='#8cb3ca',width=2)
  d.text((270,y+41),node,font=font(23),fill='white',anchor='mm')
  if i<2:d.text((270,y+105),'↓',font=font(26),fill='#9ef2ce',anchor='mm')
 for j,line in enumerate(wrap(d,item['narration'],font(20),470)[:5]):d.text((270,766+j*29),line,font=font(20),fill='#edf5ff',anchor='mm')
 d.rectangle((0,949,int(540*min(1,t/duration)),959),fill='#9ef2ce')
 return im
def render(item,out):
 for k in ('id','title','narration','nodes','track','quiz'):
  if k not in item:raise ValueError('missing '+k)
 if len(item['nodes'])!=3 or any(len(str(x))>40 for x in item['nodes']):raise ValueError('three short nodes required')
 out.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory() as tmp:
  wav=Path(tmp)/'voice.wav'
  subprocess.run(['espeak-ng','-s','145','-w',str(wav),item['narration']],check=True)
  probe=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(wav)],capture_output=True,text=True,check=True)
  duration=max(12.0,float(probe.stdout.strip())+1.5)
  fps=12
  cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','540x960','-r',str(fps),'-i','-','-i',str(wav),'-c:v','libx264','-preset','veryfast','-crf','27','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-t',str(duration),'-movflags','+faststart',str(out)]
  proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
  try:
   for n in range(math.ceil(duration*fps)):proc.stdin.write(frame(item,n/fps,duration).tobytes())
  finally:proc.stdin.close()
  if proc.wait()!=0:raise RuntimeError('ffmpeg rendering failed')
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--limit',type=int,default=4);args=parser.parse_args()
 catalog=json.loads((ROOT/'content/curriculum.json').read_text())['videos']
 manifest_path=ROOT/'content/manifest.json'
 try:old=json.loads(manifest_path.read_text()).get('videos',[])
 except (FileNotFoundError,json.JSONDecodeError):old=[]
 byid={v['id']:v for v in old}
 # A daily deterministic rotation; avoid re-rendering already published assets.
 import datetime
 offset=(datetime.date.today()-datetime.date(2026,11,14)).days
 candidates=[catalog[(offset+i)%len(catalog)] for i in range(min(args.limit,len(catalog)))]
 for item in candidates:
  dest=ROOT/'videos'/(item['id']+'.mp4')
  if not dest.exists():print('Rendering',item['id'],flush=True);render(item,dest)
  byid[item['id']]={**item,'video':'./videos/'+dest.name,'published_at':datetime.date.today().isoformat()}
 manifest_path.write_text(json.dumps({'videos':list(byid.values())},indent=2)+'\n')
 print('Published',len(candidates),'videos; catalog size',len(byid))
if __name__=='__main__':main()

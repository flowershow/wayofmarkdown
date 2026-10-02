import math, json
def spline(points, per=16):
    pts=[points[0]]+points+[points[-1]]; out=[]
    for i in range(1,len(pts)-2):
        p0,p1,p2,p3=pts[i-1],pts[i],pts[i+1],pts[i+2]
        for j in range(per):
            t=j/per;t2=t*t;t3=t2*t
            out.append(tuple(0.5*((2*p1[k])+(-p0[k]+p2[k])*t+(2*p0[k]-5*p1[k]+4*p2[k]-p3[k])*t2+(-p0[k]+3*p1[k]-3*p2[k]+p3[k])*t3) for k in range(2)))
    out.append(points[-1]); return out
def width_at(stops,u):
    for i in range(1,len(stops)):
        if u<=stops[i][0]:
            u0,w0=stops[i-1];u1,w1=stops[i];k=0 if u1==u0 else (u-u0)/(u1-u0)
            k=k*k*(3-2*k); return w0+(w1-w0)*k
    return stops[-1][1]
def brush(points,stops):
    pts=spline(points); arc=[0]
    for i in range(1,len(pts)): arc.append(arc[-1]+math.dist(pts[i],pts[i-1]))
    tot=arc[-1]; L=[];R=[]
    for i,p in enumerate(pts):
        a=pts[max(0,i-1)];b=pts[min(len(pts)-1,i+1)]; ln=math.dist(a,b) or 1
        nx=-(b[1]-a[1])/ln; ny=(b[0]-a[0])/ln; h=width_at(stops,arc[i]/tot)/2
        L.append((p[0]+nx*h,p[1]+ny*h)); R.append((p[0]-nx*h,p[1]-ny*h))
    # rounded loaded start: arc from R[0] around the back to L[0]
    p=pts[0]; q=pts[2]; ang=math.atan2(q[1]-p[1],q[0]-p[0]); h0=width_at(stops,0)/2
    cap=[(p[0]+math.cos(ang+math.pi/2+k*math.pi/10)*h0*1.05, p[1]+math.sin(ang+math.pi/2+k*math.pi/10)*h0*1.05) for k in range(11)]
    poly=L[::-1][:-1]+cap[::-1]+R  # end->start along L, cap, start->end along R
    poly=L+R[::-1]+cap
    d='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in poly)+'Z'
    c='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)
    return d,c,f'{tot:.1f}'
strokes=[
 # left vertical: loaded top, slight S, dry tail
 ([(41,9),(38.5,34),(35,60),(29.5,91)], [(0,10.5),(0.12,11),(0.5,9),(0.8,6),(1,0.6)]),
 # right vertical: a touch shorter, leans more
 ([(71,13),(68.5,37),(64.5,62),(59,86)], [(0,10),(0.12,10.5),(0.5,8.4),(0.8,5.6),(1,0.6)]),
 # top horizontal: rises, then lifts off
 ([(10,38.5),(34,37),(60,34.5),(91,29.5)], [(0,10),(0.1,10.5),(0.55,8),(0.85,4.8),(1,0.5)]),
 # bottom horizontal: gentle sag
 ([(8,67.5),(32,66.5),(58,65),(87,60)], [(0,10.5),(0.1,11),(0.55,8.6),(0.85,5.2),(1,0.6)]),
]
out=[brush(p,s) for p,s in strokes]
json.dump(out,open('hash.json','w'))
static='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="#1d1b19">'+''.join(f'<path d="{d}"/>' for d,_,_ in out)+'</svg>'
open('hash.svg','w').write(static)
sizes=''.join(f'<img src="hash.svg" style="width:{s}px;height:{s}px;margin:8px;vertical-align:middle">' for s in [220,64,32,16])
open('hashtest.html','w').write(f'<body style="margin:0;background:#fbf8f2">{sizes}</body>')

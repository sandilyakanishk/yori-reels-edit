import sys, wave, numpy as np
for f in sys.argv[1:]:
    w=wave.open(f); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    hop=int(sr*0.05); n=len(x)//hop
    rms=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2)+1e-12) for i in range(n)]); db=20*np.log10(rms)
    print("==",f,"dur",round(len(x)/sr,1))
    print(" level dB percentiles 5/25/50/75/95:",[round(float(np.percentile(db,p)),1) for p in (5,25,50,75,95)])
    # per-5s mean level
    print(" per-5s mean dB:",[round(float(db[i:i+100].mean()),1) for i in range(0,n,100)])
    # band energy: speech band 300-3400 vs bass <150 vs highs >6000
    N=2048; segs=[x[i:i+N]*np.hanning(N) for i in range(0,len(x)-N,N)]
    S=np.abs(np.fft.rfft(np.array(segs),axis=1))**2; fr=np.fft.rfftfreq(N,1/sr)
    tot=S.sum()
    for name,lo,hi in (("bass<150",0,150),("150-300",150,300),("voice300-3400",300,3400),("3400-8000",3400,8000)):
        print(f"  {name}: {100*S[:,(fr>=lo)&(fr<hi)].sum()/tot:.1f}%")
    # quietest stretches (floor = music bed/room when voice pauses)
    floor=np.percentile(db,5); thr=floor+8
    q=db<thr; runs=[];i=0
    while i<n:
        if q[i]:
            j=i
            while j<n and q[j]: j+=1
            if (j-i)*0.05>=0.3: runs.append((round(i*0.05,2),round((j-i)*0.05,2)))
            i=j
        else: i+=1
    print(" dips>=0.3s (start,len):",runs)
    # pitch (autocorr) on loud voiced frames
    f0=[]
    fl=int(sr*0.04)
    for i in range(0,len(x)-fl,fl):
        fr_=x[i:i+fl]
        if np.sqrt(np.mean(fr_**2))<10**(np.percentile(db,50)/20): continue
        fr_=fr_-fr_.mean(); ac=np.correlate(fr_,fr_,'full')[fl-1:]
        lo,hi=sr//300,sr//70
        k=lo+np.argmax(ac[lo:hi])
        if ac[k]>0.45*ac[0]: f0.append(sr/k)
    f0=np.array(f0)
    if len(f0): print(" pitch Hz median/10th/90th:",round(float(np.median(f0))),round(float(np.percentile(f0,10))),round(float(np.percentile(f0,90))),"n",len(f0))

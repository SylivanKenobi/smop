# Generated with SMOP  0.41-beta
from smop.libsmop import *
# generateMultiratePitchFilterbank.m

    ###############################################################################
# Generating filter bank of filters corresponding MIDI pitches
    
    # Pitches 21-59, fs = 882
# Pitches 60-95, fs = 4410
# Pitches 96-120, fs =22050
    
    # Q                  (center frequency) / bandwidt, Q > 30 separates notes
# stop:              pass_rel = 1/(2*Q); stop_rel = stop*pass_rel;
# Rp                 loses no more than Rp dB in the passband
# Rs                 attenuation in the stopband in dB
    
    # For details to filter desgin use MATLAB help function
#                    e.g., "help ellipord" and "help ellip"
    
    # Attention: Construction of [b,a] may fail if the
#                   filter specification are too restrictive
    
    
    # License:
#     This file is part of 'Chroma Toolbox'.
# 
#     'Chroma Toolbox' is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 2 of the License, or
#     (at your option) any later version.
# 
#     'Chroma Toolbox' is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with 'Chroma Toolbox'. If not, see <http://www.gnu.org/licenses/>.
# 
###############################################################################
    
# clear
semitoneOffsets=concat([0,- 0.25,- 1 / 3,- 0.5,- 2 / 3,- 0.75])
# generateMultiratePitchFilterbank.m:40
nameSuffixes=cellarray([[''],['_minusQuarter'],['_minusThird'],['_minusHalf'],['_minusTwoThird'],['_minusThreeQuarters']])
# generateMultiratePitchFilterbank.m:41
for k in arange(1,length(semitoneOffsets)).reshape(-1):
    midi=(arange(1,128))
# generateMultiratePitchFilterbank.m:46
    midi_freq=dot(2.0 ** ((midi - 69 + semitoneOffsets(k)) / 12),440)
# generateMultiratePitchFilterbank.m:47
    nameSuffix=nameSuffixes[k]
# generateMultiratePitchFilterbank.m:48
    h[120]=struct('a',[],'b',[])
# generateMultiratePitchFilterbank.m:49
    disp(concat(['Generating Filterbank: ',nameSuffix]))
    # fs = 22005, pitches 96-120
###############################################################################
    fs=22050
# generateMultiratePitchFilterbank.m:55
    nyq=fs / 2
# generateMultiratePitchFilterbank.m:56
    midi_min=96
# generateMultiratePitchFilterbank.m:57
    midi_max=120
# generateMultiratePitchFilterbank.m:58
    Q=25
# generateMultiratePitchFilterbank.m:59
    stop=2
# generateMultiratePitchFilterbank.m:59
    Rp=1
# generateMultiratePitchFilterbank.m:59
    Rs=50
# generateMultiratePitchFilterbank.m:59
    pass_rel=1 / (dot(2,Q))
# generateMultiratePitchFilterbank.m:60
    stop_rel=dot(pass_rel,stop)
# generateMultiratePitchFilterbank.m:61
    for k in arange(midi_min,midi_max).reshape(-1):
        pitch=midi_freq(k)
# generateMultiratePitchFilterbank.m:64
        Wp=concat([pitch - dot(pass_rel,pitch),pitch + dot(pass_rel,pitch)]) / nyq
# generateMultiratePitchFilterbank.m:65
        Ws=concat([pitch - dot(stop_rel,pitch),pitch + dot(stop_rel,pitch)]) / nyq
# generateMultiratePitchFilterbank.m:66
        n,Wn=ellipord(Wp,Ws,Rp,Rs,nargout=2)
# generateMultiratePitchFilterbank.m:67
        h(k).b,h(k).a=ellip(n,Rp,Rs,Wn,nargout=2)
# generateMultiratePitchFilterbank.m:68
    num=midi_max - midi_min + 1
# generateMultiratePitchFilterbank.m:70
    h_fvtool=cell(dot(2,num),1)
# generateMultiratePitchFilterbank.m:71
    for i in arange(1,num).reshape(-1):
        h_fvtool[dot(2,i) - 1]=h(midi_min + i - 1).b
# generateMultiratePitchFilterbank.m:73
        h_fvtool[dot(2,i)]=h(midi_min + i - 1).a
# generateMultiratePitchFilterbank.m:74
    fvtool(h_fvtool[arange()])
    # fs = 4410, pitches 60-95
###############################################################################
    fs=4410
# generateMultiratePitchFilterbank.m:81
    nyq=fs / 2
# generateMultiratePitchFilterbank.m:82
    midi_min=60
# generateMultiratePitchFilterbank.m:83
    midi_max=95
# generateMultiratePitchFilterbank.m:84
    Q=25
# generateMultiratePitchFilterbank.m:85
    stop=2
# generateMultiratePitchFilterbank.m:85
    Rp=1
# generateMultiratePitchFilterbank.m:85
    Rs=50
# generateMultiratePitchFilterbank.m:85
    pass_rel=1 / (dot(2,Q))
# generateMultiratePitchFilterbank.m:86
    stop_rel=dot(pass_rel,stop)
# generateMultiratePitchFilterbank.m:87
    for k in arange(midi_min,midi_max).reshape(-1):
        pitch=midi_freq(k)
# generateMultiratePitchFilterbank.m:90
        Wp=concat([pitch - dot(pass_rel,pitch),pitch + dot(pass_rel,pitch)]) / nyq
# generateMultiratePitchFilterbank.m:91
        Ws=concat([pitch - dot(stop_rel,pitch),pitch + dot(stop_rel,pitch)]) / nyq
# generateMultiratePitchFilterbank.m:92
        n,Wn=ellipord(Wp,Ws,Rp,Rs,nargout=2)
# generateMultiratePitchFilterbank.m:93
        h(k).b,h(k).a=ellip(n,Rp,Rs,Wn,nargout=2)
# generateMultiratePitchFilterbank.m:94
    num=midi_max - midi_min + 1
# generateMultiratePitchFilterbank.m:96
    h_fvtool=cell(dot(2,num),1)
# generateMultiratePitchFilterbank.m:97
    for i in arange(1,num).reshape(-1):
        h_fvtool[dot(2,i) - 1]=h(midi_min + i - 1).b
# generateMultiratePitchFilterbank.m:99
        h_fvtool[dot(2,i)]=h(midi_min + i - 1).a
# generateMultiratePitchFilterbank.m:100
    fvtool(h_fvtool[arange()])
    # fs = 882, pitches 21-59
###############################################################################
    fs=882
# generateMultiratePitchFilterbank.m:107
    nyq=fs / 2
# generateMultiratePitchFilterbank.m:108
    midi_min=21
# generateMultiratePitchFilterbank.m:109
    midi_max=59
# generateMultiratePitchFilterbank.m:110
    Q=25
# generateMultiratePitchFilterbank.m:111
    stop=2
# generateMultiratePitchFilterbank.m:111
    Rp=1
# generateMultiratePitchFilterbank.m:111
    Rs=50
# generateMultiratePitchFilterbank.m:111
    pass_rel=1 / (dot(2,Q))
# generateMultiratePitchFilterbank.m:112
    stop_rel=dot(pass_rel,stop)
# generateMultiratePitchFilterbank.m:113
    for k in arange(midi_min,midi_max).reshape(-1):
        pitch=midi_freq(k)
# generateMultiratePitchFilterbank.m:116
        Wp=concat([pitch - dot(pass_rel,pitch),pitch + dot(pass_rel,pitch)]) / nyq
# generateMultiratePitchFilterbank.m:117
        Ws=concat([pitch - dot(stop_rel,pitch),pitch + dot(stop_rel,pitch)]) / nyq
# generateMultiratePitchFilterbank.m:118
        n,Wn=ellipord(Wp,Ws,Rp,Rs,nargout=2)
# generateMultiratePitchFilterbank.m:119
        h(k).b,h(k).a=ellip(n,Rp,Rs,Wn,nargout=2)
# generateMultiratePitchFilterbank.m:120
    num=midi_max - midi_min + 1
# generateMultiratePitchFilterbank.m:122
    h_fvtool=cell(dot(2,num),1)
# generateMultiratePitchFilterbank.m:123
    for i in arange(1,num).reshape(-1):
        h_fvtool[dot(2,i) - 1]=h(midi_min + i - 1).b
# generateMultiratePitchFilterbank.m:125
        h_fvtool[dot(2,i)]=h(midi_min + i - 1).a
# generateMultiratePitchFilterbank.m:126
    fvtool(h_fvtool[arange()])
    save(concat(['MIDI_FB_ellip_pitch_60_96_22050_Q25',nameSuffix]),'h','-V6')
    
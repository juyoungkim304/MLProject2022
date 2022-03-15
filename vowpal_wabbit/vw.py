import sys
from vowpalwabbit import pyvw

if_train = sys.argv[1]
fv_file = sys.argv[2]
model_file = sys.argv[3]
predict_file = sys.argv[4]

if if_train == '1':
  vw = pyvw.Workspace(
          quiet=False,
          k=True,
          c=True,
          indexing=0,
          oaa=2,
          #ect=2,
          #learning rate
          l=0.1,
          #epochs
          passes=50,
          holdout_off=True,
          d=fv_file,
          f=model_file,
          #bigrams rn - can test a few
          ngram="w2",
          #skipgrams - 1
          #skips="w1",
          #classweight="-1:0.1",
          spelling="w",
          #affix="+1w,+2w,-1w,-2w",
          b=28,
          noconstant=True,
  )
else :
  vw = pyvw.Workspace(
        quiet=True,
        t=True,
        d=fv_file,
        i=model_file,
        p=predict_file,
        ring_size=100000,
  )

for f in *.edge
do
 fi=${f%.edge}
 python dimacs2ffhtd.py -f $f >$fi.hg
done

#! /bin/sh

trainFullPath=$1
# Order of the model? Good values from 1 to 6,7
order=$2
# How many iterations? Usually 10
iter=$3
# Quadratic penalty: Can set to 0.5, 0, or some other value
qpenalty=$4
# The w in the paper: 4 and 6 were tested in the paper
csize=$5


trainFile=`basename $trainFullPath`
trainDir=`dirname $trainFullPath`

doAlign=True

# need to specify path to the M2M aligner
# EDIT THIS TO YOUR LOCAL PATH
path2M2M=~/projects/OCR/OCR/m2m-aligner-master/

# we replace | to PIPE. Be sure to change that back
sed -e 's/|/PIPE/g' ${trainFullPath} > ${trainFullPath}.nopipe

if [ $doAlign = True ]; then
  $path2M2M/m2m-aligner --sepInChar "_MYJOIN_" --sepChar "|" -i ${trainFullPath}.nopipe --maxX 1 --maxY 2 --delX --nullChar "EMPTY"
fi

alignFile="${trainFile}.nopipe.m-mAlign.1-2.delX.1-best.conYX.align"
alignFullPath=$trainDir/$alignFile

./removeLast.py < $alignFullPath > ${alignFullPath}.rl

# that's a hack
# Marmot doesn't like ":" and we also replace "-"
sed -i -e 's/:/COLON/g' ${alignFullPath}.rl
sed -i -e 's/-/DASH/g' ${alignFullPath}.rl # insert this in

# now we train
./makeModel-segmenter-order_complex.sh ${alignFullPath}.rl ${order} ${iter} ${qpenalty} ${csize}

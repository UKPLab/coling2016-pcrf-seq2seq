#! /bin/sh

testFile=$1
model=$2
window=$3

outfile=`basename $testFile`

echo $testFile $model $window

sed -i -e 's/:/COLON/g' ${testFile}
sed -i -e 's/|/PIPE/g' ${testFile}

sed -i -e 's/-/DASH/g' ${testFile}

./decode-simple_dev.sh $testFile $model $window ${outfile}

predFile=OUTPUTS_dev3/${outfile}.pred
sed -e 's/_MYJOIN_/ /g' ${predFile} | sed -e 's/COLON/:/g' | sed -e 's/PIPE/|/g' | sed -e 's/DASH/-/g'

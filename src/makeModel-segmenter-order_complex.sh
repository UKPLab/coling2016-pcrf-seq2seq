#! /bin/bash

# SAMPLE USAGE:
# ./makeModel-simple.sh ~/projects/G2P_higherOrderCRF/Data/Aligned/train80000.dat.clear.m-mAlign.1-2.delX.1-best.conYX.align.imp 4 10 0.5

input=$1
order=$2
numIter=$3
qpenalty=$4
csize=$5
inputfile=
for i in $(echo $input | tr "/" "\n")
do
  inputfile=$i
done

if [ -z $input ] || [ -z $order ]; then
  echo "./makeModel-segmenter-order.sh <fullPathToAlignedFile> <order>"
  exit
fi

tmpTrain=tmp/train_crf.dat

# EDIT THIS TO YOUR LOCAL PATH
marmotTagger=~/projects/marmot/marmot-2015-06-12.jar

if [ -f $tmpTrain ]; then
    tmpTrain=$tmpTrain.`date +%s`
fi

# make CRF format for test and train file ##################
echo "Creating training data for alignments with features ..."
./makeAlign-seg_complex.py ${csize} ${csize} < "${input}" > ${tmpTrain}

# train the CRF ###############################
echo "Training marmot aligner on train data ..."
trainFile=`pwd`/${tmpTrain}
java -Xmx120G -cp ${marmotTagger} marmot.morph.cmd.Trainer -train-file form-index=0,tag-index=1,token-feature-index=2,${trainFile} -order ${order} -tag-morph false -model-file MODELS_cl/${inputfile}-align.marmot-${order}-${numIter}-${qpenalty}-${csize} \
  -num-iterations $numIter -quadratic-penalty ${qpenalty} -verbose true 


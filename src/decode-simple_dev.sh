#! /bin/bash

fullpath=$1
input=$1
inputfile=
for i in $(echo $fullpath | tr "/" "\n")
do
  inputfile=$i
  #echo ${i}
done

modelFileAlign=$2
window=$3
outfile=$4

OUTDIR=OUTPUTS_dev3

if [ -z "$inputfile" ] || [ -z "$modelFileAlign" ]; then
  echo "./decode.sh <fullPathInputFile> <modelFileAlign>";
  echo "$inputfile" "$modelFileAlign" "$modelFileSeg" "$nseg" "$nalign"
  exit
fi

# EDIT THIS TO YOUR LOCAL PATH
marmotTagger=~/projects/marmot/marmot-2015-06-12.jar

# segment x strings in CRF format #####################
tmpFile=tmp/${inputfile}_${window}.seg.out.feat
if [ ! -f ${tmpFile} ]; then
  echo "Creating segmentation data for testing ..."
  ./makeSeg_complex.py $window $window < "$input" > ${tmpFile}
else
  echo "Was already segmented."
fi

# tagging
testFile=`pwd`/${tmpFile}
mod=$(basename ${modelFileAlign})
java -cp ${marmotTagger} marmot.morph.cmd.Annotator --model-file ${modelFileAlign} --test-file form-index=0,token-feature-index=2,${testFile} --pred-file tmp/${inputfile}_${mod}.align 

./extractStrings.py < tmp/${inputfile}_${mod}.align > ${OUTDIR}/${outfile}.pred


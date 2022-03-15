# java Split 3 cleanedTrainingVowpal-2.txt tokenizedTrainingVowpal-2.txt
# java Split 3 cleanedValidationVowpal-2.txt tokenizedValidationVowpal-2.txt
cp cleanedTrainingVowpal-2.txt tokenizedTrainingVowpal-2.txt
cp cleanedValidationVowpal-2.txt tokenizedValidationVowpal-2.txt
python vw.py 1 tokenizedTrainingVowpal-2.txt model2 prediction2.txt
python vw.py 0 tokenizedValidationVowpal-2.txt model2 prediction2.txt
python evaluation.py

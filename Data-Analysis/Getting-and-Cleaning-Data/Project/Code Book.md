Cleaning-Data
=============

Repo for Cleaning Data Class on Coursera

Feature Selection 
=================

The features selected for this database come from the accelerometer and gyroscope 3-axial raw signals tAcc-XYZ and tGyro-XYZ. These time domain signals (prefix 't' to denote time) were captured at a constant rate of 50 Hz. Then they were filtered using a median filter and a 3rd order low pass Butterworth filter with a corner frequency of 20 Hz to remove noise. Similarly, the acceleration signal was then separated into body and gravity acceleration signals (tBodyAcc-XYZ and tGravityAcc-XYZ) using another low pass Butterworth filter with a corner frequency of 0.3 Hz. 

Subsequently, the body linear acceleration and angular velocity were derived in time to obtain Jerk signals (tBodyAccJerk-XYZ and tBodyGyroJerk-XYZ). Also the magnitude of these three-dimensional signals were calculated using the Euclidean norm (tBodyAccMag, tGravityAccMag, tBodyAccJerkMag, tBodyGyroMag, tBodyGyroJerkMag). 

Finally a Fast Fourier Transform (FFT) was applied to some of these signals producing fBodyAcc-XYZ, fBodyAccJerk-XYZ, fBodyGyro-XYZ, fBodyAccJerkMag, fBodyGyroMag, fBodyGyroJerkMag. (Note the 'f' to indicate frequency domain signals). 

These signals were used to estimate variables of the feature vector for each pattern:  
'-XYZ' is used to denote 3-axial signals in the X, Y and Z directions.

In this case the variables used were those about mean and standard deviation measurements.
The List of all the variables used can be found in the last section. 


Data Cleaning and Variable Extraction
===============================================
To clean the data the following steps were taken

1) Loaded the following File in R, from the train and test folder
    Train files: Y_train.txt, X_train.txt, subject_train
    Test files: Y_test.txt, X_test.txt, subject_test
    Features.txt (to get the names for the X_train and X_test data)
    activity_labels.txt (to get the names 

2) Added a Column to the Y_train and Y_test data frames to display
   both the activity code and the associated activity. The two new data frames
   were called Updated_Y_train and Updated_X_train
   
3) Renamed the column in the subject_train and subject_test data frames
   as subject_ID
   
4) Combined the train and test datasets for X, Y and subject separately.
   The following dataframes were obtained:
    - unfiltered_X (combining X_train and X_test)
    - Y (combining Updated_Y_train and Updated_Y_test)
    - subject (combining subject_train and subject_test)

5) Rename the new subject dataframe column as "ID"

6) Filtered the variables in the X Unfiltered_X data frame to only the 
   columns that would contain the string "mean()" or "std()". This was 
   done because the excercise required to get only the mean and standard
   deviation measurements. The new dataframe X (with only the filtered 
   columns) was then created
   
7) Combined the three data frames subject, Y and X


List of Variables
==================

+ ID 
+ activity_code
+ activity
+ tBodyAcc-mean()-X
+ tBodyAcc-mean()-Y
+ tBodyAcc-mean()-Z
+ tBodyAcc-std()-X
+ tBodyAcc-std()-Y
+ tBodyAcc-std()-Z
+ tGravityAcc-mean()-X
+ tGravityAcc-mean()-Y
+ tGravityAcc-mean()-Z
+ tGravityAcc-std()-X
+ tGravityAcc-std()-Y
+ tGravityAcc-std()-Z
+ tBodyAccJerk-mean()-X
+ tBodyAccJerk-mean()-Y
+ tBodyAccJerk-mean()-Z
+ tBodyAccJerk-std()-X
+ tBodyAccJerk-std()-Y
+ tBodyAccJerk-std()-Z
+ tBodyGyro-mean()-X
+ tBodyGyro-mean()-Y
+ tBodyGyro-mean()-Z
+ tBodyGyro-std()-X
+ tBodyGyro-std()-Y
+ tBodyGyro-std()-Z
+ tBodyGyroJerk-mean()-X
+ tBodyGyroJerk-mean()-Y
+ tBodyGyroJerk-mean()-Z
+ tBodyGyroJerk-std()-X
+ tBodyGyroJerk-std()-Y
+ tBodyGyroJerk-std()-Z
+ tBodyAccMag-mean()
+ tBodyAccMag-std()
+ tGravityAccMag-mean()
+ tGravityAccMag-std()
+ tBodyAccJerkMag-mean()
+ tBodyAccJerkMag-std()
+ tBodyGyroMag-mean()
+ tBodyGyroMag-std()
+ tBodyGyroJerkMag-mean()
+ tBodyGyroJerkMag-std()
+ fBodyAcc-mean()-X
+ fBodyAcc-mean()-Y
+ fBodyAcc-mean()-Z
+ fBodyAcc-std()-X
+ fBodyAcc-std()-Y
+ fBodyAcc-std()-Z
+ fBodyAccJerk-mean()-X
+ fBodyAccJerk-mean()-Y
+ fBodyAccJerk-mean()-Z
+ fBodyAccJerk-std()-X
+ fBodyAccJerk-std()-Y
+ fBodyAccJerk-std()-Z
+ fBodyGyro-mean()-X
+ fBodyGyro-mean()-Y
+ fBodyGyro-mean()-Z
+ fBodyGyro-std()-X
+ fBodyGyro-std()-Y
+ fBodyGyro-std()-Z
+ fBodyAccMag-mean()
+ fBodyAccMag-std()
+ fBodyBodyAccJerkMag-mean()
+ fBodyBodyAccJerkMag-std()
+ fBodyBodyGyroMag-mean()
+ fBodyBodyGyroMag-std()
+ fBodyBodyGyroJerkMag-mean()
+ fBodyBodyGyroJerkMag-std()

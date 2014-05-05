## Helper Function to create tidy data on the Y data frame
Add_Y_labels <- function(Y_df, labels_df, column_names){
  for(i in 1:nrow(Y_df)){
    # First Iterations Create New Column and Change Column Names
    if(i == 1){
      Y_df[ncol(Y_df)+1] <- NA
      colnames(Y_df)<- c("activity_code", "activity")
    }
    for(j in 1:nrow(labels_df)){
      if(Y_df[i,1] == labels_df[j,1]){ Y_df[i,2] <- as.character(labels_df[j,2]) }
    } 
  }
  
  return(Y_df)
}

# Homework Peer Assignment - Cleaning Data

# Load the Data (Read each file separately)
train_Folder <- file.path('UCI HAR Dataset', 'train')
test_Folder <- file.path('UCI HAR Dataset', 'test')
 
subject_train <- read.table(file.path(train_Folder, "subject_train.txt"))
Y_train <- read.table(file.path(train_Folder, "Y_train.txt"))
X_train <- read.table(file.path(train_Folder, "X_train.txt"))
  
subject_test <- read.table(file.path(test_Folder, "subject_test.txt"))
Y_test <- read.table(file.path(test_Folder, "Y_test.txt"))
X_test <- read.table(file.path(test_Folder, "X_test.txt"))

# Load file with features (columns) name for X_test and X_train
X_names <- read.table(file.path('UCI HAR Dataset', 'features.txt'))
X_names <- X_names[,2]

# Add a Column to Y_train and Y_test to get activty_code and activity_name
Y_activity_labels <- read.table(file.path('UCI HAR Dataset', 'activity_labels.txt'))
Y_names <- c("activity_code", "activity")
Updated_Y_train <- Add_Y_labels(Y_train,Y_activity_labels, Y_names )
Updated_Y_test <- Add_Y_labels(Y_test,Y_activity_labels, Y_names )
subject_name <- c("subject_ID")

# Combine the train and test datasets (X, Y and subject)
unfiltered_X <- rbind(X_train, X_test)
Y <- rbind(Updated_Y_train, Updated_Y_test)
subject <- rbind(subject_train, subject_test)
  
# Name all the dataframe columns (Y is already renamed using Add_Y_labels)
colnames(unfiltered_X) <- X_names
colnames(subject) <- c("ID")

# Filter to only  variables with mean and std
means <- grep("mean\\(\\)", X_names)
stds <- grep("std\\(\\)", X_names)
relevant <- sort(c(means, stds))
X <- unfiltered_X[relevant]

# Combine (subject, Y, X) to obtain the complete dataframe
all <- cbind(subject, Y, X)

## Creates a second, independent tidy data set with the average of 
## each variable for each activity and each subject. 
require(reshape2)
df_melt <- melt(all, id = c("ID", "activity_code", "activity"))
tidy_data_set_complete <- dcast(df_melt, ID + activity_code+ activity~ variable, mean)

# Prints the tidy data frame
View(tidy_data_set_complete)

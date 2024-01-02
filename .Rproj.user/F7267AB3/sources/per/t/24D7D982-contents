# Use a relative path if the file is in the same folder as your R script
tsv_file_path <- "processed-tumour-DSP.tsv"

# Check if the file exists
if (file.exists(tsv_file_path)) {
  # Read the TSV file into a data frame
  data_frame <- read.table(tsv_file_path, header = TRUE, sep = "\t", stringsAsFactors = FALSE)
  
  # Convert the data frame to a list of lists
  list_of_lists <- lapply(as.data.frame(data_frame), as.list)
  
  # Print the list of lists
  print(list_of_lists)
} else {
  cat("Error: File not found. Please check the file path.\n")
}


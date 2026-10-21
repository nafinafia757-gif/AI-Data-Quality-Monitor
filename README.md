# AI-Data-Quality-Monitor
An AI-powered data quality monitoring system using Python, Streamlit, and DistilBERT to detect data quality issues, identify missing values and duplicates, and analyze noisy text data.
AI Data Quality Monitor

## Live Demo

Try the deployed AI Data Quality Monitor application here:

 "Launch AI Data Quality Monitor" (https://ai-data-quality-monitor-6pvidmxdery8owq7azmyxf.streamlit.app/)

## Project Overview

AI Data Quality Monitor is a data quality analysis application developed using Python, Streamlit, and Deep Learning. It helps users identify common data quality issues and analyze text data using a trained DistilBERT model.

## Objectives

- Identify missing values in datasets.
- Detect duplicate records.
- Analyze numerical outliers.
- Evaluate data quality and highlight potential issues.
- Use a trained DistilBERT model for text quality analysis.
- Generate useful insights to support data cleaning and preprocessing.

## Technologies Used

- Python
- Pandas and NumPy
- Streamlit
- PyTorch
- Hugging Face Transformers
- DistilBERT
- Scikit-learn
- Plotly
- Excel

## Dataset

The project uses the Online Retail II dataset, which contains retail transaction data from an online retail business.

Dataset file: "online_retail_II.xlsx"

## Deep Learning Model

A DistilBERT text classification model was trained using Hugging Face Transformers in Google Colab. The trained model and tokenizer were saved for use in the application.

The model is intended to support text quality analysis by identifying potentially clean and noisy text based on its training data.

## Key Features

- Interactive Streamlit dashboard
- Dataset upload and inspection
- Missing value detection
- Duplicate record detection
- Numerical outlier analysis
- Text quality analysis using DistilBERT
- Data quality insights and visualizations
- Downloadable analysis reports

## Project Workflow

1. Load or upload a dataset.
2. Inspect the dataset structure and data types.
3. Analyze missing values and duplicate records.
4. Detect potential numerical outliers.
5. Analyze text quality using the trained model.
6. Display results and insights through the Streamlit interface.


## Applications

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Retail transaction data validation
- Text data quality assessment
- Preparing datasets for machine learning workflows

## Limitations

- Analysis quality depends on the dataset and the implemented detection methods.
- DistilBERT predictions depend on the model's training data and labels.
- Large datasets and deep learning models may require additional memory and processing time.
- The application identifies potential data quality issues but does not guarantee that every issue will be detected.

## Future Enhancements

- Add more advanced data validation rules.
- Support additional dataset formats.
- Improve text classification with more diverse training data.
- Add automated data cleaning recommendations.
- Enhance dashboard reporting and deployment performance.

## Conclusion

AI Data Quality Monitor combines data analysis techniques and deep learning to help identify data quality issues in datasets. The interactive dashboard makes data inspection easier and supports better data preparation for analytics and machine learning.



Project Repository

"AI Data Quality Monitor on GitHub" (https://github.com/nafinafia757-gif/AI-Data-Quality-Monitor)

import streamlit, pandas

streamlit.title('🎂My First StreamLit App')
streamlit.header('🎂Display Food List')
streamlit.text('🎂From Amazon S3')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

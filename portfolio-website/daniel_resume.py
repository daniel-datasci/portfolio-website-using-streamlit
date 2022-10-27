import streamlit as st


#####################
# Header 
st.write('''
# Daniel Ifediba
##### *Resume* 
''')


st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Scientist/Data Analyst.
- Strong verbal and written communication skills.
- Experienced storyteller using data and visualization tools.
- Strong Knowledge of applying Machine Learning in real life scenarios and solving real time problems.
-  Passionate about data and helping others kick start their data careers.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/daniel-datasci" target="_blank">Daniel Ifediba</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
st.write('=======================================================================================')
#####################
st.markdown('''
## Education
''')

txt('**Data Science Accelerator Program**, *ExploreAI Academy*, South Africa',
'2022')

txt('**Data Science With Python**, *Simpli Learn*',
'2022')

txt('**Data Science**, *Data Camp*',
'2022')

txt('**Bachelors of Science** (Accounting), *Anambra State Univrsity*, Nigeria',
'2016')
st.write('=======================================================================================')

#####################
st.markdown('''
## Work Experience
''')

txt('**Junior Data Scientist (Internsip)**, ExploreAI, South Africa',
'Jan 2022-Present')
st.markdown('''
- Conducted assessments on reports drawn from data by building dashboards with the use of PowerBI and SQL, whose visualization gave 60% more clarity to stakeholders. 
- Successfully organized a team of 6 individuals to build a model that classifies twitter data with the use of Python and Machine Learning Algorithms.
- Applied statistical and machine learning techniques to solve diverse business problems.
''')

txt('**Founder**, CID Academy, Nigeria',
'2022')
st.markdown('''
- Helping young data professionals kick start their data careers by providing them foundational knowledge on SQL, PYTHON, POWERBI and MACHINE LEARNING
- Giving young data heroes on-the-go skills in communicating insights from visualized data.
''')

txt('**Customer Relationship Officer**, Jumia Group, Nigeria',
'July 2019- 2021')
st.markdown('''
- Provided assistance in seeking sales; spiraled sales turnover by 19% over 3 months.
- Advised canceling customers on new procedures, persuading them to stay with the company resulting in a 30% decrease in cancellation.
- Developed new methodologies in soliciting sales; increased sales and revenue turnover by 30% and 47% respectively
''')
st.write('=======================================================================================')
#####################
st.markdown('''
## Projects
''')
txt4('Retirement Income Predictor', 'Affiliated With ExploreAI', '[Project Source Code](https://github.com/daniel-datasci/Retirement-Income-Predictor)')
st.markdown('''
Most people have a certain level of uncertainty nearing retirement age, as to if they will be able to reach their retirement goals. This uncertainty comes from factors such as; savings, health, number of dependents and so on. This project aims to reduce this levels of uncertainty and give people a higher level of confidence towards retirement by helping them know what income they should amass every month to reach this goal. The type of investment choice to be chosen is also adviced.
''')
st.write('---------------------------------------------------------------------------------------------------------------------------------------------')
txt4('House Prices Prediction', 'Outsourced Project', '[Project Source Code](https://github.com/daniel-datasci/House-Prices-Prediction-1)')
st.markdown('''
Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence. This project aims to give people looking to seel or buy a house, the important factors that influece the hike or decline in price of houses.
''')
st.write('---------------------------------------------------------------------------------------------------------------------------------------------')
txt4('Sales Revenue Insights', 'Outsourced Project', '[Project Source Code](https://github.com/daniel-datasci/Sales-Insights)')
st.markdown('''
There are many times companies or simple business run into the difficulty of choosing which products they should focus on when they deal on different categories of products. This project aimed to give the said company clarity on how these various pproduct categories perform in sales over a period of 4 years. There is also a proffessional recommendation on which product should more resources be channeled to and which to be discarded.
''')
st.write('---------------------------------------------------------------------------------------------------------------------------------------------')
txt4('Other Projects', '---','[Projects Source Code](https://github.com/daniel-datasci/)')
st.write('=======================================================================================')
#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`, `Numpy`, `Excel`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Powerbi`, `Excel`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Model deployment', '`Streamlit`, `Heroku`, `AWS`')
st.write('=======================================================================================')
#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', '[Connect With Me](https://www.linkedin.com/in/daniel-ifediba-a681a4226/)')
txt2('Twitter', '[My Twitter Universe](https://twitter.com/Daniel_Ifediba)')
txt2('GitHub', '[Dive Into To My Code Archive](https://github.com/daniel-datasci/)')
txt2('Email Address', 'danifedibah@gmail.com')
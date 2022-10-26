import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Daniel Ifediba, Ph.D.
##### *Resume* 
''')

image = Image.open('my_image.JPEG')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Data Scientist/Data Analyst
- Strong verbal and written communication skills.
- Experienced storyteller using data and visualization tools.
- Strong Knowledge of applying Machine Learning in real life scenarios and solving real time problems.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
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
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
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

#####################
st.markdown('''
## Education
''')

txt('**Data Science Accelerator Program**, *ExploreAI Academy*, South Africa',
'2022')
st.markdown('''
- GPA: `3.89`
- Research thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
- Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
- Thesis awarded `1st` Prize by the National Research Council of Thailand.
''')

txt('**Data Science With Python**, *Simpli Learn*',
'2022')

txt('**Data Science**, *Data Camp*',
'2022')

txt('**Bachelors of Science** (Accounting), *Anambra State Univrsity*, Nigeria',
'2016')


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

#####################
st.markdown('''
## Bioinformatics Tools
''')
txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`, `Numpy`, `Excel`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`, `Powerbi`, `Excel`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Model deployment', '`Streamlit`, `Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/daniel-ifediba-a681a4226/')
txt2('Twitter', 'https://twitter.com/Daniel_Ifediba')
txt2('GitHub', 'https://github.com/daniel-datasci/')
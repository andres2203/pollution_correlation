Pollution Correlation with public transportation and growing population

IRONHACK Project work related on the public transportation

1. Description

    Today, 3.6 billion people (https://www.mckinsey.com/featured-insights/urbanization/how-to-make-a-city-great) are living in cities. By 2030, that number is expected to reach 5 billion. That means that by 2030, 60 percent of the world’s population will live in cities.

    Considering this forecast and the increasing constitution of Megacities, air quality as become one of the most important indicators of lifequality.
    
    For this reason, we have collected data from thre different cities: Madrid, Berlin and Hong Kong. For each of them we gathered:
    - historical pollution data for the following pollutants: CO(mg/m3), NO_2(µg/m3), NOx(µg/m3), O_3(µg/m3), PM10(µg/m3), PM25(µg/m3), SO_2(µg/m3). Max granularity is daily.
    - yearly population
    - public transport length (km)  

2. Folders and Files
    - FOLDERS:
        - Hong Kong Data: 
            - HK_pollution_data: all .csv's with the historical pollution info of Hong Kong
            - HK pollution index.ipynb: notebook were the pollution csv have been merged in single df, cleaned and formated
            - Hong Kong Population.ipynb: notebook were HK's population has been webscrapped
        - pollution_madrid: all .csv's with the historical pollution info of Madrid
        - pickles:
            - berlin_pollution: exported file with cleaned berlin pollution
            - berlin_population: exported file with cleaned berlin population
            - combined_dataframe: pkl with single df that concat merged_pollution and merged_population
            - hk_pollution: exported file with cleaned hong kong pollution
            - hk_population: exported file with cleaned hong kong population
            - madrid_pollution: exported file with cleaned madrid pollution
            - madrid_population: exported file with cleaned madrid population
            - merged_pollution: pkl with single df concat berlin_pollution, madrid_pollution and hk_pollution
            - merged_population: pkl with single df concat berlin_population, madrid_population and hk_population
    - Files:
        - .gitignore
        - DS_Store
        - Berlin-Data: notebook that automatically downloads, opens and cleans data about berlin's pollution from guvernamental website
        - DataFrame_Pollution_population: notebook that imports merged_pollution and merged_population and concats them in a single df
        - Merged pollution: notebook that imports berlin_pollution, madrid_pollution and hk_pollution and concats them in a single df
        - Merged population: notebook that imports berlin_population, madrid_population and hk_population and concats them in a single df
        - Plotting_Pollution: notebook that imports merged pollution and plots the evolution of the pollutants in time for each of the three cities.
        - README.md: you are reading me! ;)
        - pollution_mad: notebook were the pollution .csv's have been merged in single df, cleaned and formated 
        - population_berlin: notebook were Berlin's population has been obtained through API, cleaned and formated in single df
        - population_mad: notebook were Madrid's population has been webscrapped, cleaned and formated in single df
        - public_transport_cities: notebook were public transport information for the three cities has been webscrapped, cleaned and formated in single df

3. Results


4. Python libraries used:

    - Pandas
    - Numpy
    - requests
    - json
    - BeautifulSoup
    - re
    - matplotlib

5. Sources for the information collected:

    - Honk Kong:
        - Pollution: https://cd.epic.epd.gov.hk/EPICDI/air/station/
        - Population: https://www.ceicdata.com/en/indicator/hong-kong/population
        - Public transport: https://www.gov.hk/en/about/abouthk/factsheets/docs/transport.pdf
    - Berlin:
        - Pollution: https://luftdaten.berlin.de/station/overview/active
        - Population: https://www.destatis.de/DE/Service/OpenData/api-webservice.html 
        - Public transport: https://en.wikipedia.org/wiki/Berlin 
    - Madrid:
        - Pollution: https://datos.madrid.es/portal/site/egob 
        - Population: https://datosmacro.expansion.com/demografia/poblacion/espana-comunidades-autonomas/madrid 
        - Public transport:
            - https://en.wikipedia.org/wiki/Madrid
            - https://www.crtm.es/tu-transporte-publico/ 

6. Environment dependancies:
    - appnope==0.1.0
    - asn1crypto==1.2.0
    - attrs==19.2.0
    - backcall==0.1.0
    - beautifulsoup4==4.8.1
    - bleach==3.1.0
    - certifi==2019.9.11
    - cffi==1.13.0
    - chardet==3.0.4
    - colorama==0.4.1
    - cryptography==2.8
    - cycler==0.10.0
    - decorator==4.4.0
    - defusedxml==0.6.0
    - entrypoints==0.3
    - idna==2.8
    - ipykernel==5.1.2
    - ipython==7.8.0
    - ipython-genutils==0.2.0
    - jedi==0.15.1
    - Jinja2==2.10.3
    - joblib==0.13.2
    - jsonschema==3.0.2
    - jupyter-client==5.3.3
    - jupyter-core==4.5.0
    - kiwisolver==1.1.0
    - langdetect==1.0.7
    - MarkupSafe==1.1.1
    - matplotlib==3.1.1
    - mistune==0.8.4
    - mkl-fft==1.0.14
    - mkl-random==1.1.0
    - mkl-service==2.3.0
    - nbconvert==5.6.0
    - nbformat==4.4.0
    - notebook==6.0.1
    - numpy==1.17.2
    - pandas==0.25.1
    - pandocfilters==1.4.2
    - parso==0.5.1
    - pexpect==4.7.0
    - pickleshare==0.7.5
    - prometheus-client==0.7.1
    - prompt-toolkit==2.0.10
    - ptyprocess==0.6.0
    - pycountry==19.8.18
    - pycparser==2.19
    - Pygments==2.4.2
    - PyMySQL==0.9.3
    - pyOpenSSL==19.0.0
    - pyparsing==2.4.2
    - pyrsistent==0.15.4
    - ySocks==1.7.1
    - python-dateutil==2.8.0
    - pytz==2019.3
    - pyzmq==18.1.0
    - requests==2.22.0
    - scikit-learn==0.21.3
    - scipy==1.3.1
    - Send2Trash==1.5.0
    - six==1.12.0
    - soupsieve==1.9.3
    - SQLAlchemy==1.3.10
    - terminado==0.8.2
    - testpath==0.4.2
    - tornado==6.0.3
    - traitlets==4.3.3
    - urllib3==1.24.2
    - wcwidth==0.1.7
    - webencodings==0.5.1
    - xlrd==1.2.0
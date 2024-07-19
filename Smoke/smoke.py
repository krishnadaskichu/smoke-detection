import streamlit as st
import pickle
from PIL import Image

def main():
    import streamlit as st
    st.markdown("<h1 style='text-align: center; color: red;'>Smoke Detection</h1>", unsafe_allow_html=True)
    st.divider()
    st.write("Smoke detection systems are designed to identify the presence of smoke, typically as an indicator of fire. These systems can range from simple devices like smoke detectors in homes to complex systems using advanced technology for industrial applications. ")

    image=Image.open('IMG_7205.JPG')
    st.image(image,width=800)
    model=pickle.load(open('smoke_detection.pkl','rb'))
    scaler=pickle.load(open('minmaxscaler','rb'))
    #utc,temperature,humidity,TVOC[ppb],Raw H2,Raw Ethanol,Pressure[hPa],PM1.0,NC0.5,Fire Alarm
#utc=Timestamp UTC seconds
#temperature=Air Temperature
#humidity=Air Humidity
#TVOC[ppb]=otal Volatile Organic Compounds; measured in parts per billion
#RawH2=raw molecular hydrogen; not compensated (Bias, temperature, etc.
#Raw ethanol=raw ethanol gas
#Pressure[hPa]=Air pressure
#PM1.0=particulate matter size < 1.0 µm (PM1.0). 1.0 µm < 2.5 µm (PM2.5)
#NC0.5=Number concentration of particulate matter. This differs from PM because NC gives the actual number of particles in
    st.markdown("<h4 style='text-align: center; color: gray;'>Enter below details for smoke detection :</h4>", unsafe_allow_html=True)
    utc=st.text_input("Timestamp UTC seconds"," ")
    temperature=st.text_input("Air Temperature","")
    humidity=st.text_input("Air Humidity","")
    TVOC=st.text_input("Total Volatile Organic Compounds","")
    RawH2=st.text_input("Raw Molecular Hydrogen","")
    Rawethanol=st.text_input("Raw ethanol Gas","")
    Pressure=st.text_input("Air pressure","")
    PM1=st.text_input("particulate matter size < 1.0 µm","")
    NC0=st.text_input("Number concentration of particulate matter","")
    pred=st.button('PREDICT')
    if pred:
        prediction=model.predict(scaler.transform([[int(utc),float(temperature),float(humidity),float(TVOC),int(RawH2),int(Rawethanol),float(Pressure),float(PM1),float(NC0)]]))
        if prediction==0:
            st.header("There is no chance of Fire")
        else:
            st.header("There is a chance of Fire")
    st.divider()
    st.subheader("To Preventing smoke and fire incidents :")
    st.markdown("* Place smoke detectors on every level of your home, including inside and outside sleeping areas. For commercial and industrial settings")
    st.markdown("* Install and maintain an integrated alarm system that includes smoke, heat, and carbon monoxide detectors.")
    st.markdown("* Test smoke detectors monthly and replace batteries at least once a year. Replace smoke detectors every 10 years.")
    st.markdown("* Public Awareness and Education: Educate family members, employees, and the community about fire safety practices.")
    st.markdown("* Keep fire extinguishers in easily accessible locations.")
    st.markdown("* Do not overload electrical outlets or power strips.")



main()
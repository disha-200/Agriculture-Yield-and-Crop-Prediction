import numpy as np
import pandas as pd

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]



dictionary_crops={'Arecanut':1, 'Other Kharif pulses':2, 'Rice':3, 'Banana':4, 'Cashewnut':5,
       'Coconut ':6, 'Dry ginger':7, 'Sugarcane':8, 'Sweet potato':9, 'Tapioca':10,
       'Black pepper':11, 'Dry chillies':12, 'other oilseeds':13, 'Turmeric':14,
       'Maize':15, 'Moong(Green Gram)':16, 'Urad':17, 'Arhar/Tur':18, 'Groundnut':19,
       'Sunflower':20, 'Bajra':21, 'Castor seed':22, 'Cotton(lint)':23, 'Horse-gram':24,
       'Jowar':25, 'Korra':26, 'Ragi':27, 'Tobacco':28, 'Gram':29, 'Wheat':30, 'Masoor':31,
       'Sesamum':32, 'Linseed':33, 'Safflower':34, 'Onion':35, 'other misc. pulses':36,
       'Samai':37, 'Small millets':38, 'Coriander':39, 'Potato':40,
       'Other  Rabi pulses':41, 'Soyabean':42, 'Beans & Mutter(Vegetable)':43,
       'Bhindi':44, 'Brinjal':45, 'Citrus Fruit':46, 'Cucumber':47, 'Grapes':48, 'Mango':49,
       'Orange':50, 'other fibres':51, 'Other Fresh Fruits':52, 'Other Vegetables':53,
       'Papaya':54, 'Pome Fruit':55, 'Tomato':56, 'Mesta':57, 'Cowpea(Lobia)':58,
       'Lemon':59, 'Pome Granet':60, 'Sapota':61, 'Cabbage':62, 'Rapeseed &Mustard':63,
       'Peas  (vegetable)':64, 'Niger seed':65, 'Bottle Gourd':66, 'Varagu':67,
       'Garlic':68, 'Ginger':69, 'Oilseeds total':70, 'Pulses total':71, 'Jute':72,
       'Peas & beans (Pulses)':73, 'Blackgram':74, 'Paddy':75, 'Pineapple':76,
       'Barley':77, 'Sannhamp':78, 'Khesari':79, 'Guar seed':80, 'Moth':81,
       'Other Cereals & Millets':82, 'Cond-spcs other':83, 'Turnip':84, 'Carrot':85,
       'Redish':86, 'Arcanut (Processed)':87, 'Atcanut (Raw)':88,
       'Cashewnut Processed':89, 'Cashewnut Raw':90, 'Cardamom':91, 'Rubber':92,
       'Bitter Gourd':93, 'Drum Stick':94, 'Jack Fruit':95, 'Snak Guard':96, 'Tea':97,
       'Coffee':98, 'Cauliflower':99, 'Other Citrus Fruit':100, 'Water Melon':101,
       'Total foodgrain':102, 'Kapas':103, 'Colocosia':104, 'Lentil':105, 'Bean':106,
       'Jobster':107, 'Perilla':108, 'Rajmash Kholar':109, 'Ricebean (nagadal)':110,
       'Ash Gourd':111, 'Beet Root':112, 'Lab-Lab':113, 'Ribed Guard':114, 'Yam':115,
       'Pump Kin':116, 'Apple':117, 'Peach':118, 'Pear':119, 'Plums':120, 'Litchi':121, 'Ber':122,
       'Other Dry Fruit':123, 'Jute & mesta':124}


dictionary_season={'Kharif':1, 'Whole Year':2, 'Autumn':3, 'Rabi':4,
       'Summer':5, 'Winter':6}


dictionary_states={'Andaman and Nicobar Islands':1, 'Andhra Pradesh':2,
       'Arunachal Pradesh':3, 'Assam':4, 'Bihar':5, 'Chandigarh':6,
       'Chhattisgarh':7, 'Dadra and Nagar Haveli':8, 'Goa':9, 'Gujarat':10,
       'Haryana':11, 'Himachal Pradesh':12, 'Jammu and Kashmir':13, 'Jharkhand':14,
       'Karnataka':15, 'Kerala':16, 'Madhya Pradesh':17, 'Maharashtra':18, 'Manipur':19,
       'Meghalaya':20, 'Mizoram':21, 'Nagaland':22, 'Odisha':23, 'Puducherry':24,
       'Punjab':25, 'Rajasthan':26, 'Sikkim':27, 'Tamil Nadu':28, 'Telangana':29,
       'Tripura':30, 'Uttar Pradesh':31, 'Uttarakhand':32, 'West Bengal':33}


dictionary_districts={'NICOBARS':1, 'NORTH AND MIDDLE ANDAMAN':2, 'SOUTH ANDAMANS':3,
       'ANANTAPUR':4, 'CHITTOOR':5, 'EAST GODAVARI':6, 'GUNTUR':7, 'KADAPA':8,
       'KRISHNA':9, 'KURNOOL':10, 'PRAKASAM':11, 'SPSR NELLORE':12, 'SRIKAKULAM':13,
       'VISAKHAPATANAM':14, 'VIZIANAGARAM':15, 'WEST GODAVARI':16, 'ANJAW':17,
       'CHANGLANG':18, 'DIBANG VALLEY':19, 'EAST KAMENG':20, 'EAST SIANG':21,
       'KURUNG KUMEY':22, 'LOHIT':23, 'LONGDING':24, 'LOWER DIBANG VALLEY':25,
       'LOWER SUBANSIRI':26, 'NAMSAI':27, 'PAPUM PARE':28, 'TAWANG':29, 'TIRAP':30,
       'UPPER SIANG':31, 'UPPER SUBANSIRI':32, 'WEST KAMENG':33, 'WEST SIANG':34,
       'BAKSA':35, 'BARPETA':36, 'BONGAIGAON':37, 'CACHAR':38, 'CHIRANG':39, 'DARRANG':40,
       'DHEMAJI':41, 'DHUBRI':42, 'DIBRUGARH':43, 'DIMA HASAO':44, 'GOALPARA':45,
       'GOLAGHAT':46, 'HAILAKANDI':47, 'JORHAT':48, 'KAMRUP':49, 'KAMRUP METRO':50,
       'KARBI ANGLONG':51, 'KARIMGANJ':52, 'KOKRAJHAR':53, 'LAKHIMPUR':54, 'MARIGAON':55,
       'NAGAON':56, 'NALBARI':57, 'SIVASAGAR':58, 'SONITPUR':59, 'TINSUKIA':60,
       'UDALGURI':61, 'ARARIA':62, 'ARWAL':63, 'AURANGABAD':64, 'BANKA':65, 'BEGUSARAI':66,
       'BHAGALPUR':67, 'BHOJPUR':68, 'BUXAR':69, 'DARBHANGA':70, 'GAYA':71, 'GOPALGANJ':72,
       'JAMUI':73, 'JEHANABAD':74, 'KAIMUR (BHABUA)':75, 'KATIHAR':76, 'KHAGARIA':77,
       'KISHANGANJ':78, 'LAKHISARAI':79, 'MADHEPURA':80, 'MADHUBANI':81, 'MUNGER':82,
       'MUZAFFARPUR':83, 'NALANDA':84, 'NAWADA':85, 'PASHCHIM CHAMPARAN':86, 'PATNA':87,
       'PURBI CHAMPARAN':88, 'PURNIA':89, 'ROHTAS':90, 'SAHARSA':91, 'SAMASTIPUR':92,
       'SARAN':93, 'SHEIKHPURA':94, 'SHEOHAR':95, 'SITAMARHI':96, 'SIWAN':97, 'SUPAUL':98,
       'VAISHALI':99, 'CHANDIGARH':100, 'BALOD':101, 'BALODA BAZAR':102, 'BALRAMPUR':103,
       'BASTAR':104, 'BEMETARA':105, 'BIJAPUR':106, 'BILASPUR':107, 'DANTEWADA':108,
       'DHAMTARI':109, 'DURG':110, 'GARIYABAND':111, 'JANJGIR-CHAMPA':112, 'JASHPUR':113,
       'KABIRDHAM':114, 'KANKER':115, 'KONDAGAON':116, 'KORBA':117, 'KOREA':118, 'MAHASAMUND':119,
       'MUNGELI':120, 'NARAYANPUR':121, 'RAIGARH':122, 'RAIPUR':123, 'RAJNANDGAON':124,
       'SUKMA':125, 'SURAJPUR':126, 'SURGUJA':127, 'DADRA AND NAGAR HAVELI':128,
       'NORTH GOA':129, 'SOUTH GOA':130, 'AHMADABAD':131, 'AMRELI':132, 'ANAND':133,
       'BANAS KANTHA':134, 'BHARUCH':135, 'BHAVNAGAR':136, 'DANG':137, 'DOHAD':138,
       'GANDHINAGAR':139, 'JAMNAGAR':140, 'JUNAGADH':141, 'KACHCHH':142, 'KHEDA':143,
       'MAHESANA':144, 'NARMADA':145, 'NAVSARI':146, 'PANCH MAHALS':147, 'PATAN':148,
       'PORBANDAR':149, 'RAJKOT':150, 'SABAR KANTHA':151, 'SURAT':152, 'SURENDRANAGAR':153,
       'TAPI':154, 'VADODARA':155, 'VALSAD':156, 'AMBALA':157, 'BHIWANI':158, 'FARIDABAD':159,
       'FATEHABAD':160, 'GURGAON':161, 'HISAR':162, 'JHAJJAR':163, 'JIND':164, 'KAITHAL':165,
       'KARNAL':166, 'KURUKSHETRA':167, 'MAHENDRAGARH':168, 'MEWAT':169, 'PALWAL':170,
       'PANCHKULA':171, 'PANIPAT':172, 'REWARI':173, 'ROHTAK':174, 'SIRSA':175, 'SONIPAT':176,
       'YAMUNANAGAR':177, 'CHAMBA':178, 'HAMIRPUR':179, 'KANGRA':180, 'KINNAUR':181, 'KULLU':182,
       'LAHUL AND SPITI':183, 'MANDI':184, 'SHIMLA':185, 'SIRMAUR':186, 'SOLAN':187, 'UNA':188,
       'ANANTNAG':189, 'BADGAM':190, 'BANDIPORA':191, 'BARAMULLA':192, 'DODA':193,
       'GANDERBAL':194, 'JAMMU':195, 'KARGIL':196, 'KATHUA':197, 'KISHTWAR':198, 'KULGAM':199,
       'KUPWARA':200, 'LEH LADAKH':201, 'POONCH':202, 'PULWAMA':203, 'RAJAURI':204, 'RAMBAN':205,
       'REASI':206, 'SAMBA':207, 'SHOPIAN':208, 'SRINAGAR':209, 'UDHAMPUR':210, 'BOKARO':211,
       'CHATRA':212, 'DEOGHAR':213, 'DHANBAD':214, 'DUMKA':215, 'EAST SINGHBUM':216, 'GARHWA':217,
       'GIRIDIH':218, 'GODDA':219, 'GUMLA':220, 'HAZARIBAGH':221, 'JAMTARA':222, 'KHUNTI':223,
       'KODERMA':224, 'LATEHAR':225, 'LOHARDAGA':226, 'PAKUR':227, 'PALAMU':228, 'RAMGARH':229,
       'RANCHI':230, 'SAHEBGANJ':231, 'SARAIKELA KHARSAWAN':232, 'SIMDEGA':233,
       'WEST SINGHBHUM':234, 'BAGALKOT':235, 'BANGALORE RURAL':236, 'BELGAUM':238,
       'BELLARY':239, 'BENGALURU URBAN':240, 'BIDAR':241, 'CHAMARAJANAGAR':242,
       'CHIKBALLAPUR':243, 'CHIKMAGALUR':244, 'CHITRADURGA':245, 'DAKSHIN KANNAD':246,
       'DAVANGERE':247, 'DHARWAD':248, 'GADAG':249, 'GULBARGA':250, 'HASSAN':251, 'HAVERI':252,
       'KODAGU':253, 'KOLAR':254, 'KOPPAL':255, 'MANDYA':256, 'MYSORE':257, 'RAICHUR':258,
       'RAMANAGARA':259, 'SHIMOGA':260, 'TUMKUR':261, 'UDUPI':262, 'UTTAR KANNAD':263,
       'YADGIR':264, 'ALAPPUZHA':265, 'ERNAKULAM':266, 'IDUKKI':267, 'KANNUR':268,
       'KASARAGOD':269, 'KOLLAM':270, 'KOTTAYAM':271, 'KOZHIKODE':272, 'MALAPPURAM':273,
       'PALAKKAD':274, 'PATHANAMTHITTA':275, 'THIRUVANANTHAPURAM':276, 'THRISSUR':277,
       'WAYANAD':278, 'AGAR MALWA':279, 'ALIRAJPUR':280, 'ANUPPUR':281, 'ASHOKNAGAR':282,
       'BALAGHAT':283, 'BARWANI':284, 'BETUL':285, 'BHIND':286, 'BHOPAL':287, 'BURHANPUR':288,
       'CHHATARPUR':289, 'CHHINDWARA':290, 'DAMOH':291, 'DATIA':292, 'DEWAS':293, 'DHAR':294,
       'DINDORI':295, 'GUNA':296, 'GWALIOR':297, 'HARDA':298, 'HOSHANGABAD':299, 'INDORE':300,
       'JABALPUR':301, 'JHABUA':302, 'KATNI':303, 'KHANDWA':304, 'KHARGONE':305, 'MANDLA':306,
       'MANDSAUR':307, 'MORENA':308, 'NARSINGHPUR':309, 'NEEMUCH':310, 'PANNA':311, 'RAISEN':312,
       'RAJGARH':313, 'RATLAM':314, 'REWA':315, 'SAGAR':316, 'SATNA':317, 'SEHORE':318, 'SEONI':319,
       'SHAHDOL':320, 'SHAJAPUR':321, 'SHEOPUR':322, 'SHIVPURI':323, 'SIDHI':324, 'SINGRAULI':325,
       'TIKAMGARH':326, 'UJJAIN':327, 'UMARIA':328, 'VIDISHA':329, 'AHMEDNAGAR':330, 'AKOLA':331,
       'AMRAVATI':332, 'BEED':333, 'BHANDARA':334, 'BULDHANA':335, 'CHANDRAPUR':336, 'DHULE':337,
       'GADCHIROLI':338, 'GONDIA':339, 'HINGOLI':340, 'JALGAON':341, 'JALNA':342, 'KOLHAPUR':343,
       'LATUR':344, 'MUMBAI':345, 'NAGPUR':346, 'NANDED':347, 'NANDURBAR':348, 'NASHIK':349,
       'OSMANABAD':350, 'PALGHAR':351, 'PARBHANI':352, 'PUNE':353, 'RAIGAD':354, 'RATNAGIRI':355,
       'SANGLI':356, 'SATARA':357, 'SINDHUDURG':358, 'SOLAPUR':359, 'THANE':360, 'WARDHA':361,
       'WASHIM':362, 'YAVATMAL':363, 'BISHNUPUR':364, 'CHANDEL':365, 'CHURACHANDPUR':366,
       'IMPHAL EAST':367, 'IMPHAL WEST':368, 'SENAPATI':369, 'TAMENGLONG':370, 'THOUBAL':371,
       'UKHRUL':372, 'EAST GARO HILLS':373, 'EAST JAINTIA HILLS':374,
       'EAST KHASI HILLS':375, 'NORTH GARO HILLS':376, 'RI BHOI':377,
       'SOUTH GARO HILLS':378, 'SOUTH WEST GARO HILLS':379,
       'SOUTH WEST KHASI HILLS':380, 'WEST GARO HILLS':381, 'WEST JAINTIA HILLS':382,
       'WEST KHASI HILLS':383, 'AIZAWL':384, 'CHAMPHAI':385, 'KOLASIB':386, 'LAWNGTLAI':387,
       'LUNGLEI':388, 'MAMIT':389, 'SAIHA':390, 'SERCHHIP':391, 'DIMAPUR':392, 'KIPHIRE':393,
       'KOHIMA':394, 'LONGLENG':395, 'MOKOKCHUNG':396, 'MON':397, 'PEREN':398, 'PHEK':399,
       'TUENSANG':400, 'WOKHA':401, 'ZUNHEBOTO':402, 'ANUGUL':403, 'BALANGIR':404,
       'BALESHWAR':405, 'BARGARH':406, 'BHADRAK':407, 'BOUDH':408, 'CUTTACK':409, 'DEOGARH':410,
       'DHENKANAL':411, 'GAJAPATI':412, 'GANJAM':413, 'JAGATSINGHAPUR':414, 'JAJAPUR':415,
       'JHARSUGUDA':416, 'KALAHANDI':417, 'KANDHAMAL':418, 'KENDRAPARA':419, 'KENDUJHAR':420,
       'KHORDHA':421, 'KORAPUT':422, 'MALKANGIRI':423, 'MAYURBHANJ':424, 'NABARANGPUR':425,
       'NAYAGARH':426, 'NUAPADA':427, 'PURI':428, 'RAYAGADA':429, 'SAMBALPUR':430, 'SONEPUR':431,
       'SUNDARGARH':432, 'KARAIKAL':433, 'MAHE':434, 'PONDICHERRY':435, 'YANAM':436,
       'AMRITSAR':437, 'BARNALA':438, 'BATHINDA':439, 'FARIDKOT':440, 'FATEHGARH SAHIB':441,
       'FAZILKA':442, 'FIROZEPUR':443, 'GURDASPUR':444, 'HOSHIARPUR':445, 'JALANDHAR':446,
       'KAPURTHALA':447, 'LUDHIANA':448, 'MANSA':449, 'MOGA':450, 'MUKTSAR':451, 'NAWANSHAHR':452,
       'PATHANKOT':453, 'PATIALA':454, 'RUPNAGAR':455, 'S.A.S NAGAR':456, 'SANGRUR':457,
       'TARN TARAN':458, 'AJMER':459, 'ALWAR':460, 'BANSWARA':461, 'BARAN':462, 'BARMER':463,
       'BHARATPUR':464, 'BHILWARA':465, 'BIKANER':466, 'BUNDI':467, 'CHITTORGARH':468,
       'CHURU':469, 'DAUSA':470, 'DHOLPUR':471, 'DUNGARPUR':472, 'GANGANAGAR':473,
       'HANUMANGARH':474, 'JAIPUR':475, 'JAISALMER':476, 'JALORE':477, 'JHALAWAR':479,
       'JHUNJHUNU':480, 'JODHPUR':481, 'KARAULI':482, 'KOTA':483 ,'NAGAUR':484, 'PALI':485,
       'PRATAPGARH':486, 'RAJSAMAND':487, 'SAWAI MADHOPUR':488, 'SIKAR':489, 'SIROHI':490,
       'TONK':491, 'UDAIPUR':492, 'EAST DISTRICT':493, 'NORTH DISTRICT':494,
       'SOUTH DISTRICT':495, 'WEST DISTRICT':496, 'ARIYALUR':497, 'COIMBATORE':498,
       'CUDDALORE':499, 'DHARMAPURI':500, 'DINDIGUL':501, 'ERODE':502, 'KANCHIPURAM':503,
       'KANNIYAKUMARI':504, 'KARUR':505, 'KRISHNAGIRI':506 ,'MADURAI':507, 'NAGAPATTINAM':508,
       'NAMAKKAL':509, 'PERAMBALUR':510, 'PUDUKKOTTAI':511, 'RAMANATHAPURAM':512, 'SALEM':513,
       'SIVAGANGA':514, 'THANJAVUR':515, 'THE NILGIRIS':516, 'THENI':517, 'THIRUVALLUR':518,
       'THIRUVARUR':519, 'TIRUCHIRAPPALLI':520, 'TIRUNELVELI':521, 'TIRUPPUR':523,
       'TIRUVANNAMALAI':524, 'TUTICORIN':525, 'VELLORE':526, 'VILLUPURAM':527,
       'VIRUDHUNAGAR':528, 'ADILABAD':529, 'HYDERABAD':530, 'KARIMNAGAR':531, 'KHAMMAM':532,
       'MAHBUBNAGAR':533, 'MEDAK':534, 'NALGONDA':535, 'NIZAMABAD':536, 'RANGAREDDI':537,
       'WARANGAL':538, 'DHALAI':539, 'GOMATI':540, 'KHOWAI':541, 'NORTH TRIPURA':542,
       'SEPAHIJALA':543, 'SOUTH TRIPURA':544, 'UNAKOTI':545, 'WEST TRIPURA':546, 'AGRA':547,
       'ALIGARH':548, 'ALLAHABAD':549, 'AMBEDKAR NAGAR':550, 'AMETHI':551, 'AMROHA':552,
       'AURAIYA':553, 'AZAMGARH':554, 'BAGHPAT':555, 'BAHRAICH':556, 'BALLIA':557, 'BANDA':558,
       'BARABANKI':559, 'BAREILLY':560, 'BASTI':561, 'BIJNOR':562, 'BUDAUN':563,
       'BULANDSHAHR':564, 'CHANDAULI':565, 'CHITRAKOOT':566, 'DEORIA':567, 'ETAH':568,
       'ETAWAH':569, 'FAIZABAD':570, 'FARRUKHABAD':571, 'FATEHPUR':572, 'FIROZABAD':573,
       'GAUTAM BUDDHA NAGAR':574, 'GHAZIABAD':575, 'GHAZIPUR':576, 'GONDA':577,
       'GORAKHPUR':578, 'HAPUR':579, 'HARDOI':580, 'HATHRAS':581, 'JALAUN':582, 'JAUNPUR':583,
       'JHANSI':584, 'KANNAUJ':585, 'KANPUR DEHAT':586, 'KANPUR NAGAR':587, 'KASGANJ':588,
       'KAUSHAMBI':589, 'KHERI':590, 'KUSHI NAGAR':591, 'LALITPUR':592, 'LUCKNOW':593,
       'MAHARAJGANJ':594, 'MAHOBA':595, 'MAINPURI':596, 'MATHURA':597, 'MAU':598, 'MEERUT':599,
       'MIRZAPUR':600, 'MORADABAD':601, 'MUZAFFARNAGAR':602, 'PILIBHIT':603, 'RAE BARELI':604,
       'RAMPUR':605, 'SAHARANPUR':606, 'SAMBHAL':607, 'SANT KABEER NAGAR':608,
       'SANT RAVIDAS NAGAR':609, 'SHAHJAHANPUR':610, 'SHAMLI':611, 'SHRAVASTI':612,
       'SIDDHARTH NAGAR':613, 'SITAPUR':614, 'SONBHADRA':615, 'SULTANPUR':616, 'UNNAO':617,
       'VARANASI':618, 'ALMORA':619, 'BAGESHWAR':620, 'CHAMOLI':621, 'CHAMPAWAT':622,
       'DEHRADUN':623, 'HARIDWAR':624, 'NAINITAL':625, 'PAURI GARHWAL':626, 'PITHORAGARH':627,
       'RUDRA PRAYAG':628, 'TEHRI GARHWAL':629, 'UDAM SINGH NAGAR':630, 'UTTAR KASHI':631,
       '24 PARAGANAS NORTH':632, '24 PARAGANAS SOUTH':633, 'BANKURA':634, 'BARDHAMAN':635,
       'BIRBHUM':636, 'COOCHBEHAR':637, 'DARJEELING':638, 'DINAJPUR DAKSHIN':639,
       'DINAJPUR UTTAR':640, 'HOOGHLY':641, 'HOWRAH':642, 'JALPAIGURI':643, 'MALDAH':644,
       'MEDINIPUR EAST':645, 'MEDINIPUR WEST':646, 'MURSHIDABAD':647, 'NADIA':648,
       'PURULIA':649}



dictionary_crops_new={'rice':1, 'maize':2, 'chickpea':3, 'kidneybeans':4, 'pigeonpeas':5,
       'mothbeans':6, 'mungbean':7, 'blackgram':8, 'lentil':8, 'pomegranate':10,
       'banana':11, 'mango':12, 'grapes':13, 'watermelon':14, 'muskmelon':15, 'apple':16,
       'orange':17, 'papaya':18, 'coconut':19, 'cotton':20, 'jute':21, 'coffee':22}


from flask import Flask, request, jsonify, render_template
import joblib

model1 = joblib.load('final_pickle_model_yield.pkl')

model2 = joblib.load('final_pickle_model_crop.pkl')

app = Flask(__name__) #initialize flask


@app.route('/')
def home(): #button code
    return render_template('register.html') 


@app.route('/register',methods=['POST'])  #register code
def register():
    

    int_features2 = [str(x) for x in request.form.values()]

    r1=int_features2[0]
    print(r1)
    
    r2=int_features2[1]
    print(r2)
    logu1=int_features2[0] #userid
    passw1=int_features2[1] #paasword
        
    

    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()

    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list1.append(str(row1[0]))
                      

                      
    print(gmail_list1)
    if logu1 in gmail_list1:
        return render_template('register.html',text="This Username is Already in Use ")
    else:


              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)" 
                  val = (r1, r2) 
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                  return render_template('register.html',text="Succesfully Registered")
   

                      


    
   
@app.route('/login')
def login(): #button code
    return render_template('login.html') 


@app.route('/logedin',methods=['POST'])
def logedin(): #after logged in
    
    int_features3 = [str(x) for x in request.form.values()] 
    print(int_features3)
    logu=int_features3[0] #user id 
    passw=int_features3[1] #password


    import MySQLdb #pip install pymysqldb==0.10.1


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()

    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0])) 
                      

                      
    print(gmail_list)
    

    cursor1= db.cursor()
    cursor1.execute("SELECT password FROM user_register")
    result2=cursor1.fetchall()

    for row2 in result2:
                      print(row2)
                      print(row2[0])
                      password_list.append(str(row2[0]))
                      

                      
    print(password_list)
    print(gmail_list.index(logu))
    print(password_list.index(passw))
    
    if gmail_list.index(logu)==password_list.index(passw):
        return render_template('yield.html')
    else:
        return render_template('login.html',text='Use Proper Username and Password')
                  
                                               






@app.route('/production',methods=['POST'])  #predict the result of crop advise
def production():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]
    print(int_features1)
    a=int_features1

    
    state=a[0]
    district=a[1]
    season=a[2]
    crop=a[3]
    area=int(a[4])

    data= {'State Name':[state],'District Name':[district],'Season':[season],'Crop':[crop],'Area':[area]} 
    df = pd.DataFrame(data)
    print(df)
    
    df['State Name']=df['State Name'].map(dictionary_states)
    df['District Name']=df['District Name'].map(dictionary_districts)
    df['Season']=df['Season'].map(dictionary_season)
    df['Crop']=df['Crop'].map(dictionary_crops)


     
    prediction = model1.predict(df)
    prediction=int(prediction)
    print(prediction)
    


    return render_template('yield.html', prediction_text='You will get Yield of {} Quintal'.format(prediction))




@app.route('/yield1')
def yield1(): #button code
    return render_template('yield.html') 
   
@app.route('/crop')
def crop(): #button code
    return render_template('crop.html') 
    
@app.route('/crop_prediction',methods=['POST'])  #predict the result of crop advise
def crop_prediction():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]
    print(int_features1)
    a=int_features1
 
    temp=float(a[0])
    humid=float(a[1])
    pH=float(a[2])
    rainfall=float((a[3]))

    data= {'Temperature':[temp],'Humidity':[humid],'pH':[pH],'Rainfall':[rainfall]} 
    df = pd.DataFrame(data)
    print(df)
    
    prediction = model2.predict(df)
    prediction=int(prediction)
    print(prediction)

    print(dictionary_crops_new)
    resultcrop= {value:key for key, value in dictionary_crops_new.items()}
    
    outputcrop=(resultcrop[int(prediction)])
    print(outputcrop)

    return render_template('crop.html', prediction_text='You Can Grow {} Crop to get more yield'.format(outputcrop))

if __name__ == "__main__":
    app.run(debug=False)




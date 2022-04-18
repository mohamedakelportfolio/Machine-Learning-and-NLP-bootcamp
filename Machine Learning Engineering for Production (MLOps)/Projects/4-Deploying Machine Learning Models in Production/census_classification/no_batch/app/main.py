import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

census_app = FastAPI(title="census_income predicting")


class CensusIncome(BaseModel):
    
    
	age: int
	fnlwgt: int
	education_num: int
	capital_gain: int
	capital_loss: int
	hours_per_week: int
	workclass___: int
	workclass__federal_gov: int
	workclass__local_gov: int
	workclass__never_worked: int
	workclass__private: int
	workclass__self_emp_inc: int
	workclass__self_emp_not_inc: int
	workclass__state_gov: int
	workclass__without_pay: int
	marital_status__divorced: int
	marital_status__married_af_spouse: int
	marital_status__married_civ_spouse: int
	marital_status__married_spouse_absent: int
	marital_status__never_married: int
	marital_status__separated: int
	marital_status__widowed: int
	occupation___: int
	occupation__adm_clerical: int
	occupation__armed_forces: int
	occupation__craft_repair: int
	occupation__exec_managerial: int
	occupation__farming_fishing: int
	occupation__handlers_cleaners: int
	occupation__machine_op_inspct: int
	occupation__other_service: int
	occupation__priv_house_serv: int
	occupation__prof_specialty: int
	occupation__protective_serv: int
	occupation__sales: int
	occupation__tech_support: int
	occupation__transport_moving: int
	relationship__husband: int
	relationship__not_in_family: int
	relationship__other_relative: int
	relationship__own_child: int
	relationship__unmarried: int
	relationship__wife: int
	race__amer_indian_eskimo: int
	race__asian_pac_islander: int
	race__black: int
	race__other: int
	race__white: int
	sex__female: int
	sex__male: int
	native_country___: int
	native_country__cambodia: int
	native_country__canada: int
	native_country__china: int
	native_country__columbia: int
	native_country__cuba: int
	native_country__dominican_republic: int
	native_country__ecuador: int
	native_country__el_salvador: int
	native_country__england: int
	native_country__france: int
	native_country__germany: int
	native_country__greece: int
	native_country__guatemala: int
	native_country__haiti: int
	native_country__holand_netherlands: int
	native_country__honduras: int
	native_country__hong: int
	native_country__hungary: int
	native_country__india: int
	native_country__iran: int
	native_country__ireland: int
	native_country__italy: int
	native_country__jamaica: int
	native_country__japan: int
	native_country__laos: int
	native_country__mexico: int
	native_country__nicaragua: int
	native_country__outlying_us_guam_usvi_etc_: int
	native_country__peru: int
	native_country__philippines: int
	native_country__poland: int
	native_country__portugal: int
	native_country__puerto_rico: int
	native_country__scotland: int
	native_country__south: int
	native_country__taiwan: int
	native_country__thailand: int
	native_country__trinadad_tobago: int
	native_country__united_states: int
	native_country__vietnam: int
	native_country__yugoslavia: int
	
		

@census_app.on_event("startup")
def load_model():
    # Load classifier from pickle file
    with open("/app/census.pkl", "rb") as model:
        global rf_model
        rf_model = pickle.load(model)

@census_app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http//localhost80/docs"

@census_app.post("/predict")
def predict(census_income: CensusIncome):
    
    data_point = np.array(
		[
			[
				census_income.age,
				census_income.fnlwgt,
				census_income.education_num,
				census_income.capital_gain,
				census_income.capital_loss,
				census_income.hours_per_week,
				census_income.workclass___,
				census_income.workclass__federal_gov,
				census_income.workclass__local_gov,
				census_income.workclass__never_worked,
				census_income.workclass__private,
				census_income.workclass__self_emp_inc,
				census_income.workclass__self_emp_not_inc,
				census_income.workclass__state_gov,
				census_income.workclass__without_pay,
				census_income.marital_status__divorced,
				census_income.marital_status__married_af_spouse,
				census_income.marital_status__married_civ_spouse,
				census_income.marital_status__married_spouse_absent,
				census_income.marital_status__never_married,
				census_income.marital_status__separated,
				census_income.marital_status__widowed ,
				census_income.occupation___ ,
				census_income.occupation__adm_clerical ,
				census_income.occupation__armed_forces ,
				census_income.occupation__craft_repair ,
				census_income.occupation__exec_managerial ,
				census_income.occupation__farming_fishing ,
				census_income.occupation__handlers_cleaners ,
				census_income.occupation__machine_op_inspct ,
				census_income.occupation__other_service ,
				census_income.occupation__priv_house_serv ,
				census_income.occupation__prof_specialty ,
				census_income.occupation__protective_serv ,
				census_income.occupation__sales ,
				census_income.occupation__tech_support ,
				census_income.occupation__transport_moving ,
				census_income.relationship__husband ,
				census_income.relationship__not_in_family ,
				census_income.relationship__other_relative ,
				census_income.relationship__own_child ,
				census_income.relationship__unmarried ,
				census_income.relationship__wife ,
				census_income.race__amer_indian_eskimo ,
				census_income.race__asian_pac_islander ,
				census_income.race__black ,
				census_income.race__other ,
				census_income.race__white ,
				census_income.sex__female ,
				census_income.sex__male ,
				census_income.native_country___ ,
				census_income.native_country__cambodia ,
				census_income.native_country__canada ,
				census_income.native_country__china ,
				census_income.native_country__columbia ,
				census_income.native_country__cuba ,
				census_income.native_country__dominican_republic ,
				census_income.native_country__ecuador ,
				census_income.native_country__el_salvador ,
				census_income.native_country__england ,
				census_income.native_country__france ,
				census_income.native_country__germany ,
				census_income.native_country__greece ,
				census_income.native_country__guatemala ,
				census_income.native_country__haiti ,
				census_income.native_country__holand_netherlands ,
				census_income.native_country__honduras ,
				census_income.native_country__hong ,
				census_income.native_country__hungary ,
				census_income.native_country__india ,
				census_income.native_country__iran ,
				census_income.native_country__ireland ,
				census_income.native_country__italy ,
				census_income.native_country__jamaica ,
				census_income.native_country__japan ,
				census_income.native_country__laos ,
				census_income.native_country__mexico ,
				census_income.native_country__nicaragua ,
				census_income.native_country__outlying_us_guam_usvi_etc_ ,
				census_income.native_country__peru ,
				census_income.native_country__philippines ,
				census_income.native_country__poland ,
				census_income.native_country__portugal ,
				census_income.native_country__puerto_rico ,
				census_income.native_country__scotland ,
				census_income.native_country__south ,
				census_income.native_country__taiwan ,
				census_income.native_country__thailand ,
				census_income.native_country__trinadad_tobago ,
				census_income.native_country__united_states ,
				census_income.native_country__vietnam ,
				census_income.native_country__yugoslavia 
				
			]
		]
	)
    
    pred = rf_model.predict(data_point).tolist()
    pred = pred[0]
    print(pred)
    return {"Prediction": pred}
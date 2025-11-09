"""
Provides functions for use with the Gemini API.
"""
from google import genai
import json
from dotenv import load_dotenv
import os

SICKNESS_PROMPT: str = "Using the following symptoms and user input, clean the user's input and return a JSON response in the format {\"symptoms\": [\"cough\", \"sore throat\"]}. Your output will be used as the input for a machine learning model, so your JSON response should be fully accurate and include no other information. Only produce the JSON response, nothing else. Do not include any decorational text or formatting. It should be displayed in pure, raw plain text."
POSSIBLE_SYMPTOMS: str = 'anxiety and nervousness,depression,shortness of breath,depressive or psychotic symptoms,sharp chest pain,dizziness,insomnia,abnormal involuntary movements,chest tightness,palpitations,irregular heartbeat,breathing fast,hoarse voice,sore throat,difficulty speaking,cough,nasal congestion,throat swelling,diminished hearing,lump in throat,throat feels tight,difficulty in swallowing,skin swelling,retention of urine,groin mass,leg pain,hip pain,suprapubic pain,blood in stool,lack of growth,emotional symptoms,elbow weakness,back weakness,pus in sputum,symptoms of the scrotum and testes,swelling of scrotum,pain in testicles,flatulence,pus draining from ear,jaundice,mass in scrotum,white discharge from eye,irritable infant,abusing alcohol,fainting,hostile behavior,drug abuse,sharp abdominal pain,feeling ill,vomiting,headache,nausea,diarrhea,vaginal itching,vaginal dryness,painful urination,involuntary urination,pain during intercourse,frequent urination,lower abdominal pain,vaginal discharge,blood in urine,hot flashes,intermenstrual bleeding,hand or finger pain,wrist pain,hand or finger swelling,arm pain,wrist swelling,arm stiffness or tightness,arm swelling,hand or finger stiffness or tightness,wrist stiffness or tightness,lip swelling,toothache,abnormal appearing skin,skin lesion,acne or pimples,dry lips,facial pain,mouth ulcer,skin growth,eye deviation,diminished vision,double vision,cross-eyed,symptoms of eye,pain in eye,eye moves abnormally,abnormal movement of eyelid,foreign body sensation in eye,irregular appearing scalp,swollen lymph nodes,back pain,neck pain,low back pain,pain of the anus,pain during pregnancy,pelvic pain,impotence,infant spitting up,vomiting blood,regurgitation,burning abdominal pain,restlessness,symptoms of infants,wheezing,peripheral edema,neck mass,ear pain,jaw swelling,mouth dryness,neck swelling,knee pain,foot or toe pain,bowlegged or knock-kneed,ankle pain,bones are painful,knee weakness,elbow pain,knee swelling,skin moles,knee lump or mass,weight gain,problems with movement,knee stiffness or tightness,leg swelling,foot or toe swelling,heartburn,smoking problems,muscle pain,infant feeding problem,recent weight loss,problems with shape or size of breast,underweight,difficulty eating,scanty menstrual flow,vaginal pain,vaginal redness,vulvar irritation,weakness,decreased heart rate,increased heart rate,bleeding or discharge from nipple,ringing in ear,plugged feeling in ear,itchy ear(s),frontal headache,fluid in ear,neck stiffness or tightness,spots or clouds in vision,eye redness,lacrimation,itchiness of eye,blindness,eye burns or stings,itchy eyelid,feeling cold,decreased appetite,excessive appetite,excessive anger,loss of sensation,focal weakness,slurring words,symptoms of the face,disturbance of memory,paresthesia,side pain,fever,shoulder pain,shoulder stiffness or tightness,shoulder weakness,arm cramps or spasms,shoulder swelling,tongue lesions,leg cramps or spasms,abnormal appearing tongue,ache all over,lower body pain,problems during pregnancy,spotting or bleeding during pregnancy,cramps and spasms,upper abdominal pain,stomach bloating,changes in stool appearance,unusual color or odor to urine,kidney mass,swollen abdomen,symptoms of prostate,leg stiffness or tightness,difficulty breathing,rib pain,joint pain,muscle stiffness or tightness,pallor,hand or finger lump or mass,chills,groin pain,fatigue,abdominal distention,regurgitation.1,symptoms of the kidneys,melena,flushing,coughing up sputum,seizures,delusions or hallucinations,shoulder cramps or spasms,joint stiffness or tightness,pain or soreness of breast,excessive urination at night,bleeding from eye,rectal bleeding,constipation,temper problems,coryza,wrist weakness,eye strain,hemoptysis,lymphedema,skin on leg or foot looks infected,allergic reaction,congestion in chest,muscle swelling,pus in urine,abnormal size or shape of ear,low back weakness,sleepiness,apnea,abnormal breathing sounds,excessive growth,elbow cramps or spasms,feeling hot and cold,blood clots during menstrual periods,absence of menstruation,pulling at ears,gum pain,redness in ear,fluid retention,flu-like syndrome,sinus congestion,painful sinuses,fears and phobias,recent pregnancy,uterine contractions,burning chest pain,back cramps or spasms,stiffness all over,"muscle cramps, contractures, or spasms",low back cramps or spasms,back mass or lump,nosebleed,long menstrual periods,heavy menstrual flow,unpredictable menstruation,painful menstruation,infertility,frequent menstruation,sweating,mass on eyelid,swollen eye,eyelid swelling,eyelid lesion or rash,unwanted hair,symptoms of bladder,irregular appearing nails,itching of skin,hurts to breath,nailbiting,"skin dryness, peeling, scaliness, or roughness",skin on arm or hand looks infected,skin irritation,itchy scalp,hip swelling,incontinence of stool,foot or toe cramps or spasms,warts,bumps on penis,too little hair,foot or toe lump or mass,skin rash,mass or swelling around the anus,low back swelling,ankle swelling,hip lump or mass,drainage in throat,dry or flaky scalp,premenstrual tension or irritability,feeling hot,feet turned in,foot or toe stiffness or tightness,pelvic pressure,elbow swelling,elbow stiffness or tightness,early or late onset of menopause,mass on ear,bleeding from ear,hand or finger weakness,low self-esteem,throat irritation,itching of the anus,swollen or red tonsils,irregular belly button,swollen tongue,lip sore,vulvar sore,hip stiffness or tightness,mouth pain,arm weakness,leg lump or mass,disturbance of smell or taste,discharge in stools,penis pain,loss of sex drive,obsessions and compulsions,antisocial behavior,neck cramps or spasms,pupils unequal,poor circulation,thirst,sleepwalking,skin oiliness,sneezing,bladder mass,knee cramps or spasms,premature ejaculation,leg weakness,posture problems,bleeding in mouth,tongue bleeding,change in skin mole size or color,penis redness,penile discharge,shoulder lump or mass,polyuria,cloudy eye,hysterical behavior,arm lump or mass,nightmares,bleeding gums,pain in gums,bedwetting,diaper rash,lump or mass of breast,vaginal bleeding after menopause,infrequent menstruation,mass on vulva,jaw pain,itching of scrotum,postpartum problems of the breast,eyelid retracted,hesitancy,elbow lump or mass,muscle weakness,throat redness,joint swelling,tongue pain,redness in or around nose,wrinkles on skin,foot or toe weakness,hand or finger cramps or spasms,back stiffness or tightness,wrist lump or mass,skin pain,low back stiffness or tightness,low urine output,skin on head or neck looks infected,stuttering or stammering,problems with orgasm,nose deformity,lump over jaw,sore in nose,hip weakness,back swelling,ankle stiffness or tightness,ankle weakness,neck weakness'

RESULTS_PROMPT: str = "Using the following symptoms and user input, clean the user's input and return a JSON response in the format {\"disease\": \"Common Cold\", \"home_remedy\": \"Explanation of a home remedy for the common cold here\", \"conventional_remedy\": \"Explanation\", \"otc_remedy\": \"Explanation\", \"herbal_remedy\": \"Explanation\"} where home_remedy, conventional_remedy, otc_remedy, and herbal_remedy all offer solutions to the predicted disease in their corresponding categories. You should only respond with plain text. Do not use any formatting characters or reply with anything other than that format."
EXPLAIN_DISEASES_PROMPT: str = 'Given the following three diseases, create a JSON response with one independent and unlabeled object per disease, each object containing an explanation for a "home_remedy" for the disease, a "conventional_remedy" for conventional treatment, "otc_remedy" for over-the-counter, and "herbal_remedy" for herbal treatments. You will respond with solely the JSON response following the format, with no decorational text or extra text. It should be printed in plain text without any line breaks or other characters.'

load_dotenv() #  Loads API_KEY.env
API_KEY = os.getenv("API_KEY")

def get_symptoms(user_input: str) -> list[str]:
    """
    Extracts symptoms from user input using the Gemini API.
    Returns a list of recognized symptoms.
    """
    prompt = _create_prompt(user_input)

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    # Gemini should return JSON; attempt to parse it
    try:
        data = json.loads(response.text)
        return data.get("symptoms", [])
    except (json.JSONDecodeError, AttributeError):
        print("Error: Invalid response from Gemini API:", response.text)
        return []


def get_results(user_input: str) -> list[dict]:
    """
    Returns a list of three dictionaries containing the possible diseases
    and their remedies from the user's input.
    """
    client = genai.Client(api_key=API_KEY)

    # Step 1: Get top 3 diseases from Gemini
    disease_prompt = _create_results_prompt(user_input)
    disease_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=disease_prompt
    )

    try:
        # Expecting Gemini to return a list of disease names
        diseases = json.loads(disease_response.text)
        if not isinstance(diseases, list):
            diseases = [diseases]  # fallback
    except json.JSONDecodeError:
        diseases = ["Unknown Disease 1", "Unknown Disease 2", "Unknown Disease 3"]

    # Step 2: Explain remedies for each disease
    explain_prompt = _create_explain_disease_prompt(diseases[:3])
    explain_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=explain_prompt
    )

    try:
        results = json.loads(explain_response.text)
        # Ensure exactly 3 results
        while len(results) < 3:
            results.append({
                "disease": "Unknown",
                "home_remedy": "Could not determine",
                "conventional_remedy": "Could not determine",
                "otc_remedy": "Could not determine",
                "herbal_remedy": "Could not determine"
            })
    except json.JSONDecodeError:
        results = [{
            "disease": "Unknown",
            "home_remedy": "Could not determine",
            "conventional_remedy": "Could not determine",
            "otc_remedy": "Could not determine",
            "herbal_remedy": "Could not determine"
        }] * 3

    return results

    


def _create_prompt(user_input: str) -> str:
    """
    Creates a formatted prompt for the Gemini API based on user input.
    It requests a JSON response containing possible symptoms.
    """
    return f'{SICKNESS_PROMPT}\
            \n\
            USER INPUT: {user_input}\
            \n\
            POSSIBLE SYMPTOMS: {POSSIBLE_SYMPTOMS}'


def _create_results_prompt(user_input: str) -> str:
    """
    Creates a formatted prompt for the Gemini API based on user input.
    It requests a JSON response containing the possible disease and its remedies.
    """
    return f'{RESULTS_PROMPT}\
            \n\
            USER INPUT: {user_input}'


def _create_explain_disease_prompt(diseases: list[str]) -> str:
    """
    Creates a formatted prompt for the Gemini API based on user input.
    It requests a JSON response containing the remedy solutions for each disease.
    """
    return f'{EXPLAIN_DISEASES_PROMPT}\n\
            {str(diseases)}'

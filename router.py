from prompts import (
    GENERAL_PROMPT,
    SALES_PROMPT,
    OPERATIONS_PROMPT,
    MARKETING_PROMPT,
    DOCUMENTATION_PROMPT,
    HR_PROMPT,
    AUTOMATION_PROMPT,
    STRATEGY_PROMPT,
    FINANCE_PROMPT,
    CUSTOMER_SUPPORT_PROMPT,
)



PROMPTS = {


"sales": SALES_PROMPT,

"operations": OPERATIONS_PROMPT,

"marketing": MARKETING_PROMPT,

"documentation": DOCUMENTATION_PROMPT,

"hr": HR_PROMPT,

"automation": AUTOMATION_PROMPT,

"strategy": STRATEGY_PROMPT,

"finance": FINANCE_PROMPT,

"support": CUSTOMER_SUPPORT_PROMPT

}



CATEGORY_WORDS = {


"sales": [

"lead",
"customer",
"client",
"prospect",
"quotation",
"quote",
"proposal",
"pricing",
"price",
"sales",
"closing",
"close deal",
"objection",
"follow up",
"follow-up",
"ghost",
"no reply",
"conversion",
"pipeline"

],



"operations":[

    "workflow",
    "process",
    "system",
    "bottleneck",
    "manual",
    "task",
    "slow",
    "messy",
    "team does not know",
    "project status",
    "tracking",
    "management",
    "deadline",
    "handover"


],



"automation":[

"automation",
"automate",
"zapier",
"make",
"api",
"bot",
"integration",
"trigger",
"workflow automation",
"ai"

],



"marketing":[

"marketing",
"content",
"instagram",
"facebook",
"ads",
"brand",
"positioning",
"offer",
"campaign",
"traffic"

],



"documentation":[

"sop",
"documentation",
"document",
"manual",
"checklist",
"knowledge",
"training document"

],



"hr":[

"employee",
"staff",
"team",
"hiring",
"hire",
"manager",
"training",
"performance"

],



"finance":[

"profit",
"revenue",
"cost",
"expense",
"budget",
"cash",
"margin",
"pricing"

],



"strategy":[

"growth",
"scale",
"scaling",
"strategy",
"expansion",
"business model",
"market"

],



"support":[

"complaint",
"refund",
"angry",
"support",
"ticket",
"customer issue"

]


}




def analyze_intent(text):


    text = text.lower()


    scores = {}


    for category, words in CATEGORY_WORDS.items():


        score = 0


        for word in words:

            if word in text:

                score += 1


        scores[category] = score



    ranked = sorted(

        scores.items(),

        key=lambda x:x[1],

        reverse=True

    )


    return ranked





def choose_prompt(text:str):


    ranked = analyze_intent(text)



    primary = ranked[0]


    if primary[1] == 0:

        return GENERAL_PROMPT



    primary_prompt = PROMPTS[primary[0]]



    # Find secondary experts

    secondary = [

        item[0]

        for item in ranked[1:3]

        if item[1] > 0

    ]



    context = f"""


PRIMARY EXPERT:

{primary[0]}


SECONDARY EXPERTS:

{", ".join(secondary) 
if secondary else "None"}



You must solve the problem from the primary expert perspective.

Also consider secondary expert areas when useful.



"""


    return context + primary_prompt
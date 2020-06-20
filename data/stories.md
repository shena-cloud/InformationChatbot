## search contact happy path
* greet
- utter_greet
* contact_search{"faculty_name":"Jayakrishna Raj G","contact":"email id"}
- action_contact_search
* thanks
- utter_goodbye

## search qualification happy path
* greet
- utter_greet
* qualification_search{"faculty_name":"K A Navas","qualification":"highest qualification"}
- action_qualification_search
* thanks
- utter_goodbye

## search specialisation happy path
* greet
- utter_greet
* specialisation_search{"faculty_name":"Dinesh Babu M","specialisation":"specialization"}
- action_specialisation_search
* thanks
- utter_goodbye

## search joining year happy path
* greet
- utter_greet
* year_search{"faculty_name":"Anjana P M","joining_year":"join"}
- action_joining_year_search
* thanks
- utter_goodbye

## search contact 
* contact_search{"faculty_name":"Anoob B","contact":"emailid"}
- action_contact_search

## search qualification
* qualification_search{"faculty_name":"Jobin Jose","qualification":"educational qualification"}
- action_qualification_search

## search specialisation
* specialisation_search{"faculty_name":"Sreejesh K V","specialisation":"specialisation"}
- action_specialisation_search

## search joining year
* year_search{"faculty_name":"Sajeev K Jose","joining_year":"year of joining"}
- action_joining_year_search

## search contact + faculty name
* greet
- utter_greet
* contact_search{"contact":"email id"}
- utter_ask_faculty
* inform{"faculty_name":"Jobin Jose"}
- action_contact_search
* thanks
- utter_goodbye

## search qualification + faculty name
* greet
- utter_greet
* qualification_search{"qualificaton":"qualification"}
- utter_ask_faculty
* inform{"faculty_name":"Gopika G"}
- action_qualification_search
* thanks
- utter_goodbye

## search specialisation + faculty name
* greet 
- utter_greet 
* specialisation_search{"specialisation":"specailised"}
- utter_ask_faculty
* inform{"faculty_name":"Liji C A"}
- action_specialisation_search
* thanks
- utter_goodbye

## search joining year + faculty_name
* greet 
- utter_greet
* year_search{"joining_year":"year of joining"}
- utter_ask_faculty
* inform{"faculty_name":"Binoy K P"}
- action_joining_year_search
* thanks
- utter_goodbye

## search + contact
* greet 
- utter_greet
* inform{"faculty_name":"Ajith K K"}
- utter_ask_facility
* contact_search{"contact":"mail id"}
- action_contact_search
* thanks
- utter_goodbye

## search + qualification
* greet
- utter_greet
* inform{"faculty_name":"Ramanand A C"}
- utter_ask_facility
* qualification_search{"qulaification":"educational qualification"}
- action_qualification_search
* thanks
- utter_goodbye

## search + specialisation
* greet
- utter_greet
* inform{"faculty_name":"Agnes Jacob"}
- utter_ask_facility
* specialisation_search{"specialisation":"specialization"}
- action_specialisation_search
* thanks
- utter_goodbye

## search + joning year
* greet
- utter_greet
* inform{"faculty_name":"Sajesh Kumar"}
- utter_ask_facility
* year_search{"joining_year":"year of joining"}
- action_joining_year_search
* thanks
- utter_goodbye

## New Story

* greet
- utter_greet
* contact_search{"contact":"email id"}
- utter_ask_faculty
* inform{"faculty_name":"nishil kumar p p"}
- slot{"faculty_name":"nishil kumar p p"}
- action_contact_search
* thanks
- utter_goodbye

## New Story

* greet
- utter_greet
* qualification_search{"qualification":"qualification"}
- slot{"qualification":"qualification"}
- utter_ask_faculty
* inform{"faculty_name":"jobin jose"}
- slot{"faculty_name":"jobin jose"}
- action_qualification_search
* thanks
- utter_goodbye

## New Story

* contact_search{"contact":"mail id"}
- slot{"contact":"mail id"}
- utter_ask_faculty
* inform{"faculty_name":"shiny g"}
- slot{"faculty_name":"shiny g"}
- action_contact_search
* thanks
- utter_goodbye

## New Story

* qualification_search
- utter_ask_faculty
* inform{"faculty_name":"laseena c a"}
- slot{"faculty_name":"laseena c a"}
- action_qualification_search
* goodbye
- utter_goodbye

## New Story

* year_search
- utter_ask_faculty
* inform{"faculty_name":"saritha e"}
- slot{"faculty_name":"saritha e"}
- action_joining_year_search

## New Story

* specialisation_search{"specialisation":"specialisation"}
- utter_ask_faculty
* inform{"faculty_name":"agnes jacob"}
- slot{"faculty_name":"agnes jacob"}
- action_specialisation_search

## New Story

* inform{"faculty_name":"jobin jose"}
- slot{"faculty_name":"jobin jose"}
- utter_ask_facility
* qualification_search
- action_qualification_search

## New Story

* year_search
- utter_ask_faculty
* inform{"faculty_name":"sheeba k"}
- action_joining_year_search
* contact_search{"contact":"email id"}
- utter_ask_faculty
* inform{"faculty_name":"sheeba k"}
- slot{"faculty_name":"sheeba k"}
- action_contact_search

## New Story

* greet
- utter_greet
* qualification_search{"qualification":"qualification","faculty_name":"nishil kumar p p"}
- slot{"faculty_name":"nishil kumar p p"}
- slot{"qualification":"qualification"}
* goodbye
- utter_goodbye

## New Story

* out_of_scope
- utter_rephrase
* contact_search{"contact":"mail id"}
- slot{"contact":"mail id"}
- utter_ask_faculty
* inform{"faculty_name":"amal s kannan"}
- slot{"faculty_name":"amal s kannan"}
- action_contact_search

## greet
* greet
- utter_greet

## greet and bye
* greet
- utter_greet
* goodbye
- utter_goodbye

## say goodbye
* goodbye
- utter_goodbye

## bot challenge
* bot_challenge
- utter_iamabot

## New Story

* greet
    - utter_greet
* inform{"faculty_name":"jobin jose"}
    - slot{"faculty_name":"jobin jose"}
    - utter_ask_facility
* contact_search{"contact":"mail id"}
    - slot{"contact":"mail id"}
    - action_contact_search
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* inform{"faculty_name":"nishil kumar p p"}
    - slot{"faculty_name":"nishil kumar p p"}
    - utter_ask_facility
* specialisation_search{"specialisation":"specialisation"}
    - slot{"specialisation":"specialisation"}
    - action_specialisation_search
* thanks
    - utter_goodbye

## New Story

* greet
    - utter_greet
* contact_search{"contact":"mail id"}
    - slot{"contact":"mail id"}
    - utter_ask_faculty
* inform{"faculty_name":"saritha e"}
    - slot{"faculty_name":"saritha e"}
    - action_contact_search

## New Story

* greet
    - utter_greet
* qualification_search{"qualification":"qualification"}
    - slot{"qualification":"qualification"}
    - utter_ask_faculty
* inform{"faculty_name":"A Ranjith Ram"}
    - slot{"faculty_name":"A Ranjith Ram"}
    - action_qualification_search
* thanks
    - utter_goodbye

## New Story

* qualification_search{"qualification":"qualification"}
    - slot{"qualification":"qualification"}
    - utter_ask_faculty
* inform{"faculty_name":"Liji C A"}
    - slot{"faculty_name":"Liji C A"}
    - action_qualification_search

## New Story

* contact_search{"contact":"mail id"}
    - slot{"contact":"mail id"}
    - utter_ask_faculty
* inform{"faculty_name":"a ranjith ram"}
    - slot{"faculty_name":"a ranjith ram"}
    - action_contact_search

## New Story

* greet
    - utter_greet
* inform{"faculty_name":"A Ranjith Ram"}
    - slot{"faculty_name":"A Ranjith Ram"}
    - utter_ask_facility
* qualification_search
    - action_qualification_search

## New Story

* greet
    - utter_greet
* contact_search{"contact":"mail id","faculty_name":"nishil kumar p p"}
    - slot{"contact":"mail id"}
    - slot{"faculty_name":"nishil kumar p p"}
    - action_contact_search

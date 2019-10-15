## Differential diagnosis of erythemato-squamous diseases
The diseases in this group are psoriasis, seboreic dermatitis, lichen planus, pityriasis rosea, cronic dermatitis, and pityriasis rubra pilaris. Usually a biopsy is necessary for the diagnosis but unfortunately these diseases share many histopathological features as well. Patients were first evaluated clinically with 12 features. Afterwards, skin samples were taken for the evaluation of 22 histopathological features. The values of the histopathological features are determined by an analysis of the samples under a microscope.

## Dataset
The family history feature has the value 1 if any of these diseases has been observed in the family, and 0 otherwise. 
The age feature simply represents the age of the patient.
Other feature (clinical and histopathological) was given a degree in the range of 0 to 3. Here, 0 indicates that the feature was not present, 3 indicates the largest amount possible, and 1, 2 indicate the relative intermediate values.

Number of Instances: 366
Number of Attributes: 34

Attribute Information: -- Complete attribute documentation: Clinical Attributes: (take values 0, 1, 2, 3, unless otherwise indicated) 1: erythema 2: scaling 3: definite borders 4: itching 5: koebner phenomenon 6: polygonal papules 7: follicular papules 8: oral mucosal involvement 9: knee and elbow involvement 10: scalp involvement 11: family history, (0 or 1) 34: Age (linear)

Histopathological Attributes: (take values 0, 1, 2, 3) 12: melanin incontinence 13: eosinophils in the infiltrate 14: PNL infiltrate 15: fibrosis of the papillary dermis 16: exocytosis 17: acanthosis 18: hyperkeratosis 19: parakeratosis 20: clubbing of the rete ridges 21: elongation of the rete ridges 22: thinning of the suprapapillary epidermis 23: spongiform pustule 24: munro microabcess 25: focal hypergranulosis 26: disappearance of the granular layer 27: vacuolisation and damage of basal layer 28: spongiosis 29: saw-tooth appearance of retes 30: follicular horn plug 31: perifollicular parakeratosis 32: inflammatory monoluclear inflitrate 33: band-like infiltrate

Database:  Dermatology

Class code:   Class:                  
1             psoriasis                
2             seboreic dermatitis             
3             lichen planus                   
4             pityriasis rosea                
5             cronic dermatitis                   
6             pityriasis rubra pilaris 

https://archive.ics.uci.edu/ml/datasets/dermatology

# Testing the app
Go to https://dermdetect.herokuapp.com/ 

signup with the name, email and password 

Type in the stripe test data (cardnumber: 4242 4242 4242 4242, random exp, cvc, zipcode)

You will be directed to form to fill clinical and histopathological attributes in order to classify the dermatology disease.


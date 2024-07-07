few_shot_examples_birthcert_jp = """"""
few_shot_examples_birthcert_en = """"""
few_shot_examples_birthcert_vn = """"""

few_shot_examples_receipt_en = """"""
few_shot_examples_receipt_vn = """"""
few_shot_examples_receipt_jp = [
    [
        {
            "role": "user",
            "content": """
404

GKK-(KW)
The Whole of 6/F, King Wah Centre,
Mong Kok
Tel: 21521822
[重印]

檯號: 404 人數: 2
單號: 21074642 開單員: 服務員
日期: 2017-04-23 開單時間: 19:54:56

開檯 1 $0.0
牛角上級牛肋肉（鹽蔥）(6片) 1 $85.0
葱付牛肋肉（黑椒鹽）(6片) 1 $62.0
牛舌（鹽蔥）(6片) 1 $69.0
可口可樂 1 $18.0
Asahi 生啤（M. Glass - 500ml） 1 $42.0
Asahi 生啤（M. Glass - 500ml） 1 $42.0
温泉玉子 3 $24.0
牛角野菜拼盤 1 $32.0
温泉玉子 1 $8.0
Asahi 生啤（M. Glass - 500ml） 1 $42.0
獺祭三割九分（燒）300ml 1 $228.0
牛舌（鹽蔥）(6片) 1 $69.0
牛舌（鹽蔥）(6片) 1 $69.0
獺祭三割九分（燒）300ml 1 $228.0
牛角上級牛肋肉（鹽蔥）(6片) 1 $85.0
牛角野菜拼盤 1 $32.0
獺祭三割九分（燒）720ml 1 $588.0
燒肉六品盛合（鹽蔥） 1 $218.0

項目總計： $1941.0
加一服務費 $194.1

總計： $2135.1
現金 $2200.0
找回： $64.9

訂單員：Kingk1
時間: 2017-04-23 23:04:02
機號：1 單號: 1 重印1"""
        },
        {
            "role": "assistant",
            "content": """```json
{
"company": "GKK-(KW)",
"total": "2135.1"
"date": "2017/04/23"
"address": "The Whole of 6/F, King Wah Centre, Mong Kok",
"telephone": "21521822"
"items": [
    {"name": "Opening Table Fee", "price": "0.0", "quantity": "1"},
    {"name": "牛角上級牛肋肉（鹽蔥）(6 pieces)", "price": "85.0", "quantity": "1"},
    {"name": "葱付牛肋肉（黑椒鹽）(6 pieces)", "price": "62.0", "quantity": "1"},
    {"name": "牛舌（鹽蔥）(6 pieces)", "price": "69.0", "quantity": "3"},
    {"name": "可口可樂", "price": "18.0", "quantity": "1"},
    {"name": "Asahi 生啤 (Medium Glass - 500ml)", "price": "42.0", "quantity": "3"},
    {"name": "温泉玉子", "price": "24.0", "quantity": "3"},
    {"name": "牛角野菜拼盤", "price": "32.0", "quantity": "2"},
    {"name": "獺祭三割九分（燒）(300ml)", "price": "228.0", "quantity": "2"},
    {"name": "獺祭三割九分（燒）(720ml)", "price": "588.0", "quantity": "1"},
    {"name": "燒肉六品盛合（鹽蔥）", "price": "218.0", "quantity": "1"}
  ]
}
"""
        }
    ]
]

few_shot_examples_id_card_en = """"""
few_shot_examples_id_card_fr = """"""
few_shot_examples_id_card_jp = """"""

examples_birthcert_fr_str = [
    {
        "input": """
IWIWI TVEUU
Brest
EXCERPT FROM BIRTH CERTIFICATE
c 002353 1 2022
On the twenty-fifth of October, two thousand twenty-two
at one forty-five in the afternoon
was born in Brest (Finistere)
Antoine, Louis, Jean DULAQUAIS
male
son of Gabriel, Robert, Marie DULAQUAIS
born in Brest, on the 14th of May, 1987
and of Maryse, Liliane, Jeanne JEZEQUEL
born in Brest, on the 8th of March, 1987.
For certified true copy
BREST, October 28, 2022
The delegated Civil Registrar:
Karine BOTREL
EEP
ma
""",
        "output": """
```json
{
"birth_time": "13:44",
"firstname": "Antoine, Louis, Jean",
"lastname": "DULAQUAIS",
"doc_type": "EXTRAIT D'ACTE DE NAISSANCE",
"issued_date": "2022/10/28",
"birthdate": "2022/10/25",
"sex": "Male",
}
```"""
    },
    {
        "input": """
MGP-20221020-0170-430
Nf me's
BIRTH CERTIFICATE
FULL COPY
No 001171/2022
Emma, Annie, Nathalie DONNETTE
On the fourth of September two thousand and twenty-two at eighteen hours and eighteen minutes, was born on Avenue du Professeur Robert Debré, Emma, Annie, Nathalie DONNETTE, female, to Maxime, Bernard, Léon DONNETTE, born in Courbevoie (Hauts-de-Seine) on May 2, 1992, Car Painter, who acknowledges her today and is informed of the divisible nature of the established filiation link, and to Celine, Annie JAILLANT, born in Neuilly-sur-Seine (Hauts-de-Seine) on November 4, 1991, Nurse, residing in Codognan (Gard), 395 Chemin de la Monnaie,
Drawn up on September 6, 2022 at 11 hours and 7 minutes based on the declaration of the father, who, after reading and being invited to read the document, signed with Us, Elham OUTMANI, official of the Nimes town hall, Civil Registrar by delegation of the Mayor.
Nimes,
September 13, 2022,
For a true copy,
The delegated Civil Registrar,
CIVIL STATUS
""",
        "output": """
```json
{
"birth_time": "18:18",
"firstname": "Emma, Annie, Nathalie",
"lastname": "DONNETTE",
"doc_type": "EXTRAIT D'ACTE DE NAISSANCE",
"issued_date": "2022/09/13"",
"birthdate": "2022/09/04",
"sex": "Female",
}
```"""
    },
    {
        "input": """
CITY OF
ROUBAIX
FULL COPY OF BIRTH CERTIFICATE
Year 2022 No. 2549
BIRTH CERTIFICATE No. 2549 B
Albane, Maxine, Jessie, Pauline LEGRAIN
CHILD's Surname LEGRAIN
First names: Albane, Maxine, Jessie, Pauline
Gender: female
Born on: twenty-sixth of November, two thousand and twenty-two
At: three o'clock in the afternoon
At: Roubaix (Nord), 80 Rue de Beaumont
MOTHER's Surname LEGRAIN
First names: Jessie, Fanny, Catherine, Jacqucline, Georgina
Born on: first of December 1989
At: Saint-Omer (Pas-de-Calais)
Occupation: administrative assistant
Residence: Wattrelos (Nord), 65 Rue Négrier
DECLARATION
Third party declarant Pauline, Flore, Irma DESTRIEZ, wife of LEGRAIN, 38 years old, administrative assistant, residing in Wattrelos (Nord), 65 Rue Négrier
Date and time of the document: 28th of November 2022 at 08:48
After reading and being invited to sign the document, We, Hetene CARQUIN, Civil Registrar Officer by delegation of the Mayor of Roubaix (Nord), signed with the declarant
Marginal notes:
None
The document has been properly signed. Full copy issued according to computerized process and certified conforming to the register by Us, CARQUIN Helene, Civil Registrar Officer by delegation of the Mayor of Roubaix (Nord).
Executed in Roubaix, on the 28th of November 2022
""",
        "output": """
```json
{
"birth_time": "15:00",
"firstname": "Albane, Maxine, Jessic, Pauline",
"lastname": "LEGRAIN",
"doc_type": "COPIE INTEGRALE ACTE DE NAISSANCE",
"issued_date": "2022/11/28",
"birthdate": "2022/11/26",
"sex": "Female"
}
```"""
    }
]

examples_id_card_vn_str = [
    {
        "input": """
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
SOCIALIST REPUBLIC OF VIET NAM
Independence - Freedom - Happiness

CĂN CƯỚC CÔNG DÂN
Citizen Identity Card

Số / No.: 001305011383
Họ và tên / Full name: LÊ CẨM TÚ
Ngày sinh / Date of birth: 09/04/2005
Giới tính / Sex: Nữ
Quốc tịch / Nationality: Việt Nam
Quê quán / Place of origin: Thanh Chương, Nghệ An
Nơi thường trú / Place of residence: Nhồi Dưới, Cổ Loa, Đông Anh, Hà Nội
Có giá trị đến / Date of expiry: 09/04/2030

Đặc điểm nhận dạng / Personal identification:
Nốt ruồi C: 3cm trên sau đuôi mắt trái

Ngày, tháng, năm / Date, month, year: 24/04/2022

CỤC TRƯỞNG CỤC CẢNH SÁT
QUẢN LÝ HÀNH CHÍNH VỀ TRẬT TỰ XÃ HỘI
DIRECTOR GENERAL OF THE POLICE DEPARTMENT
FOR ADMINISTRATIVE MANAGEMENT AND SOCIAL ORDER

(Signature)

Tô Văn Huệ

Ngón trỏ trái / Left index finger
Ngón trỏ phải / Right index finger
Machine Readable Zone (MRZ):

IDVNM3050113838001305011383<9
0504092F3004098VNM<<<<<<<<<<2
LE<<CAM<TU<<<<<<<<<<<<<<<<<<<
""",
        "output": """
```json
{
"id_number": "001305011383",
"name": "LÊ CẨM TÚ",
"date_birth": "09/04/2005",
"sex": "Nữ",
"nationality": "Việt Nam",
"place_of_origin": "Thanh Chương, Nghệ An",
"place_of_residence": "Nhồi Dưới, Cổ Loa, Đông Anh, Hà Nội",
"date_expiry": "09/04/2030",
"person_identification": "Nốt ruồi C: 3cm trên sau đuôi mắt trái",
"date_issued": "24/04/2022",
"mrz": "IDVNM3050113838001305011383<90504092F3004098VNM<<<<<<<<<<2LE<<CAM<TU<<<<<<<<<<<<<<<<<<<"
}
"""
    },
    {
        "input": """
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc
SOCIALIST REPUBLIC OF VIET NAM
Independence - Freedom - Happiness
CĂN CƯỚC CÔNG DÂN
Citizen Identity Card
Số / No.: 001302032960
Họ và tên / Full name: NGUYỄN TỐ ANH
Ngày sinh / Date of birth: 13/10/2002
Giới tính / Sex: Nữ
Quốc tịch / Nationality: Việt Nam
Quê quán / Place of origin: Dương Nội, Hà Đông, Hà Nội
Nơi thường trú / Place of residence: Quyết Tiến, Dương Nội, Hà Đông, Hà Nội
Có giá trị đến / Date of expiry: 13/10/2027
Đặc điểm nhận dạng / Personal identification:
Nốt ruồi C: 2cm dưới sau cánh mũi trái

Ngày, tháng, năm / Date, month, year: 29/04/2021

CỤC TRƯỞNG CỤC CẢNH SÁT
QUẢN LÝ HÀNH CHÍNH VỀ TRẬT TỰ XÃ HỘI
DIRECTOR GENERAL OF THE POLICE DEPARTMENT
FOR ADMINISTRATIVE MANAGEMENT AND SOCIAL ORDER

(Signature)

Phạm Công Nguyên

Ngón trỏ trái / Left index finger
Ngón trỏ phải / Right index finger
IDVNM3020329605001302032960<<6
0210133F2710132VNM<<<<<<<<<<<4
NGUYEN<<TO<ANH<<<<<<<<<<<<<<<<
""",
        "output": """
```json
{
"id_number": "001302032960",
"name": "NGUYỄN TỐ ANH",
"date_birth": "13/10/2002",
"sex": "Nữ",
"nationality": "Việt Nam",
"place_of_origin": "Dương Nội, Hà Đông, Hà Nội",
"place_of_residence": "Quyết Tiến, Dương Nội, Hà Đông, Hà Nội",
"date_expiry": "13/10/2027",
"person_identification": "Nốt ruồi C: 2cm dưới sau cánh mũi trái",
"date_issued": "29/04/2021",
"mrz": "IDVNM3020329605001302032960<<60210133F2710132VNM<<<<<<<<<<<4NGUYEN<<TO<ANH<<<<<<<<<<<<<<<<"
}
"""
    }
]

examples_receipt_fr_str = [
    {
        "input": """
MGP-20220801-0110-373
ALAIN AFFLELOU LES ANGLES | Bénéficiaira JEANNIN Paul
cc LECLERC | Date naiss. | 22/04/1964
30133 LES ANGLES | Fareaze | 1 impasse dela roquette
30290 | SAINT VICTOR LA COSTE
Tél 0490907803
Fax 0490909838
Agré. 302697222 :0573006001 | Assuré | JEANNIN Paul
Siren 301 E23 636  3E |  s.s | 1640489257135/16
Iaent.3 302697822 | Faux 2 prise  sn. charge | 60
3ri | Cais. gast. | Cent.
Cphtalro. | MATHIS
Ordeanance | 05/01/2022 | I.E. | 30101458
Facture r | 21196
a | LES ANGLES, le Samedi | 9 Juillet 2022
Yeus  avez 6té  regu par  Valerie c
Sphare cylindre laze tada. Dian. | Rayon
Ice:1 | +3,25 | L 14,13 | 8,63
12,1 | 2.63
Désignation | LPP BaseRO RotRO  0tTVA FU hr 2. Brut Renise | P. Net
[possier n*61641/1] | 84,00 | 84,00
CLREEY Y AMLTIECCAL | 35,83
PART CLIENT | 8,30  | EUR c.EVa Ix  | EVA | Total E.T | It E.V.A | Total Brat | 84,0 EUR
Tccal XeE | 84,00 ER.
14,33 | 0,00 EUR
Page
""",
        "output": """
```json
{
"doc_type": "Facture",
"doctor_id": "302697222",
"delivery_add": "1 impasse dela roquette 30290 SAINT VICTOR LA COSTE",
"billing_add": "",
"security_number": "1640489257135/16",
"insured": "JEANNIN Paul",
"beneficiary": "JEANNIN Paul",
"birthday": "1964/04/22",
"paid_date": "2022/07/09",
"total": "84,00",
}
```"""
    },
    {
        "input": """
 MGP-20220802-0200-307
lentillesmoinscheres.com
francais du renouvellement de lentilles sur Internet
SENSEE SAS | 140,  Boutevajd aussmann
140  Boulevard Haussmann | 75008 PARIS
75008 PARIS
Service Clients: serviceclient@lentillesmoinscheres.com
Adresse de livraison | Adresse de facturation :
Mme Catherine MILTON | Mme Catherine MILTON
96 RUE DE LA PAPETERIE | 96 RUE DE LA PAPETERIE
APPARTEMENT J105 | APPARTEMENT  J105
91100 CORBEIL'ESSONNES (FRANCE) | 91100 CORBEIL'ESSONNES
+33696956000 | (FRANCE)
+33696956000
Facture no FR4319784 du 27 juin  2022
Votre commande n° 6381589 du 27 juin  2022 a 22:49:07
Désignation produits CE | Quantité | Code l LPP | Prix t unitaire | Prix t total I HT | Taux c de TVA | Prix 1 total TTC
Ht
ACUVUE Oasys (12) (Sphérique) | 1 | Hors | 28,25 € | 28,25 € | 20& | 33,90 @
Oeil droit | TIPS
Sphére (PWR) : -6,00 (myope)
Rayon (BC) : 8,40
Diamtre (DIA) : 14,00
Frais de livraison | 4,17 @ | 4,17 € | 20& | 5,00 €
Réduction frais de livraison | 4,17 @ | 20& | - 5,00 €
Total | 28,25 € | 33,90
Facture acquittée le 27-06-2022
Taux de | Base HT Total TVA
TVA
20& | 28,25 € | 5.65 €
Sas  au capital I de 6  994 520.49  euros  Siren : : 504  595 158 - RCS Paris Numéro d'identification TVA intracommunautaire FR-91504595158 N°FINESS: : 75 26 1 1700
1/1
""",
        "output": """
```json
{
"doc_type": "Facture de lentilles",
"doctor_id": "",
"delivery_add": "96 RUE DE LA PAPETERIE APPARTEMENT J105 91100 CORBEIL'ESSONNES (FRANCE)",
"billing_add": "96 RUE DE LA PAPETERIE APPARTEMENT J105 91100 CORBEIL'ESSONNES (FRANCE)",
"security_number": "",
"insured": "Mme Catherine MILTON",
"beneficiary": "Mme Catherine MILTON",
"birthday": "",
"paid_date": "2022/06/27",
"total": "33,90",
}
```"""
    },
    {
        "input": """
lent illesmoinscheres.
.com
francais du renouvellement de lentilles sur Internet
SENSEE....
SENSEE SAS | 140,  | Foulevaydaussmann
140 Boulevard Haussmann | 75008 PARIS
75008 PARIS
Service Clients: serviceclient@tentillesmoinscheres.com
Adresse de livraison | Adresse de  facturation
Retrait dans notre réseau | Mme Linda MONTUELLE
MONTUELLE Linda | 148 RUE DU1 PRÉSIDENT WILSON
Acuitis Levallois Perret So Ouest | 92300 LEVALLOIS PERRET
C.C So Ouest 21-39, Rue d'Alsace | (FRANCE
92300 Levallois Perret | +33678797684
France
Facture n° FR4359892 du 27 juillet 2022
Votre commande n° 6441010 du 27 juillet 2022 : 21:25:49
Désignation produits CE | Quantité | Code LPP | Prix  unitaire | Prix total  HT | Taux   de TVA Prix t total TTC
HT
DAILIES TOTAL 1 (90) (Sphérique) | Hors | 58,75 € | 58,75 € | 20& | 70,50 €
Oeil droit | TIPS
Sphére (PWR) : -2,50  (myope)
Rayon (BC) : 8,50
Diamétre (DIA) : 14,10
Frais de livraison | offerts | offerts | offerts | offerts
Total | 58,75 € | 70,50 @
Facture acquittée le 27-07-2022
Taux de | Base HT Total TVA | bancaire
TVA | Carte
20& | 58,75 @ | 11,75€
Sas  s au  capital I de 6 994 520.49 euros Siren : : 504  595  158-f RCS Parisi Numéro d'identification TVA intracommunautaire : FR-91504595158  -N'FINESS: 75 26  1700
1
1/1
07 | 8 o21 149
Hontull | Limda
""",
        "output": """
```json
{
"doc_type": "Facture de lentilles",
"doctor_id": "",
"delivery_add": "Acultis Levallois Perret - So Ouest C.C So Ouest - 21-39, Rue d'Alsace 92300 Levallois Perret France",
"billing_add": "148 RUE DU PRÉSIDENT WILSON 92300 LEVALLOIS PERRET (FRANCE)",
"security_number": "",
"insured": "Mme Linda MONTUELLE",
"beneficiary": "MONTUELLE Linda",
"birthday": "",
"paid_date": "2022/07/27",
"total": "70,50",
}
```"""
    },
    {
        "input": """
MGP-20220825-0181-942 | Le mardi 23 aoút 2022
FSE/FSP No 1288
Quittance no 1-177
N° : | 772608873
R.C | APE
Siret 89494723300017 | 4778A
RENDEL VAL D'EUROPE
14. cours du Danube | Mme Christelle SAMMUT
Ctre Cial Val d'Europe | 16 RUE HADDOCK
77700 SERRIS
Email | valdeurope@rendelparis.com
Tél. 01.60.42.94.15 Fax | 77700 CHESSY
 SARL au Capital de 1000€
Acte | Désignation. | Code Qt PU TTC Tot TTC Remise | Tx | Tot  Net Base | Part | AMC1 | AMC2
V.D Organic 1.6 AS 70 Gradient blue 1  25& | 7827820 | 115.00 | 115.00 | 0.00 | 115.00 | 0.05 | 0.03 | 0.00 | 0.00
HMC Oasis
v.G Organic 1.6 AS 70 Gradient blue 1 25& 7827820 | 115.00 | 115.00 | 0.00 | 115.00 | 0.05 | 0.03 | 0.00 | 0.00
HMC Oasis
MO PAOLA RENDEL C1 00.00 | 7221483 | 119.00 | 119.00 | 0.00 | 119.00 | 0.05 | 0.03 | 0.00 | 0.00
Total Equipement NO | 349.00 | 0.00 | 349.00 | 0.09 | 0.00 | 0.00
Total de I'offre | 349.00 | 0.00 | 349.00 | 0.09 | 0.00 | 0.00
Prescripteur centre access vision 770025526 (Ordonnance du 03/02/2022) | Forfait Mutuelle | 0.00 | 0.00
PEC N° : 0
RC  | 0.00€ CLIENT SANS TP MUTUELLE (Adh : Contrat  | Total TTC | 349.00 €
Tiers-Payant | 0.00 €
Acompte... | -349.00 €
No Assuré 269051730015481
Né(e) le 21-05-1969 | Reste a Charge | 0.00 €
l/omaemme er | la mauvelle
la | farture
Vous | trauverez c:
de corechiam pour | que
monhe ie chomgemenr 
Qrdammame paur
rembaursemenf | ankiape.
Nme ArLT | d'um
beaefae
FACTURE ACQUITTEE | RENDEL VAL D'EUROPE
14  Courp du Danube
C1 Ciays val d'Europe
77760 SERRGp
Siret : :894 947 233-Tél:0 | 01.60.42.94.15
Finess 772808 873
Fournisseur conventionné auprés de. la
Caisse Régionale de Sécurité Sociale
Facture Acquittée
""",
        "output": """
```json
{
"doc_type": "Facture",
"doctor_id": "770025526",
"delivery_add": "16 RUE HADDOCK 77700 CHESSY",
"billing_add": "",
"security_number": "",
"insured": "Mme Christelle SAMMUT",
"beneficiary": "Mme Christelle SAMMUT",
"birthday": "",
"paid_date": "2022/08/23",
"total": "349,00",
}
```"""
    },
    {
        "input": """
MGP-20220901-0156-630
CENTRE COMMERCIAL CLEUNAY RUE JULES VALLES
35065 RENNES
optique | Tél 0223406920
Fax. 0223406921
E.Leclerc@ | Mail optique.renouest@socamaine.fr
FINESS 352612444
Mme. BEAUVERGER ESTELLE
Nom de I'assuré | M. | 6 IMPASSE DES ROCHELLES
.Numéro tel  | .06 44 02 87 62 | .35310 SAINT THURIAL
IDate Naiss. | 18/06/1973
Caisse :
N° Sécu Sociale : | 2°73 06 35 115 060 15
Adeli/Presc Opt : | 351771563/Dr ARCADE
Prescripteur RPPS : | 10101746658 | 010 77
9900400610003957022 | RENNES, le mardi 23 aoút 2022
Facture NF100039570 du 23/08/2022 | FACTURE ACQUITTÉE
Code Produit | Désignation | Prix Unit. prix | Qté | Remise | Montant
HT (€) | TTC (€) | TTC (€)
Conseiis de manipulation pour. ia pose, le retrait et | OFFERT
Ientretien des lentilles de contact et votre suivi
n°D100031745---
A0HM6M | Alcon. AIR OPTIX PLUS HYDRAGLYDE MULTIFOCAL AD | 38,88 | 46,65 | 1,20 € | 45,45
.MED. 6L  14.2/8.6 BOITE DE 6
-5.50
.TIPS : 39.48 € CODE  LPP GEN 2251545 CODE RGPT : LEN
:Adresse fab: Alcon 20, r.. des Deux Gares 92842 Rueil Malmaison
'AOHM6M, Alcon AIR OPTIX PLUS HYDRAGLYDE MULTIFOCAL AD I MED 6L
Caractéristiques essentielles SOUPLE, 1 MOIS, BOITE DE 6
A0HM6M | Alcon AIR 0PTIX PLUS HYDRAGLYDE MULTIFOCAL AD | 38,88 | .46,65 | 1,20 € | 45,45
MED] 6L 14.2/8.6 BOITE DE 6
-5.75
TIPS : 39.48 € CODE LPP GEN : : 2251545 CODE RGPT : LEN
Adresse fab: Alcon 20. r. des Deux Gares 92842 Rueil Malmaison
Caractéristiques identiques la lentille droite
00133407 | Bausch \ Lomb Renu 360ml | 7.08 | 8,50 | 8,50
TVA 20:00 16,57
Total HT (€) : | 82,83
Total ttc (€) | 99,40
Net a payer (€) | 99,40
Réglement
espéce | 99,40
pase | espece
a cqili. | espéce
C | 238 | 122
Hs2s | Upe
LecleRe
Mail | ca.naine.fr
C00S1
Optique E. LECLERC procede au traitement de vos données. personnelles  aux 1  fins. de  gestion. de votre commande. Les destinataires 1 | donées : sont .otre. centre C CPAM | AE
organisme de complémentaire santé. Cette collecte est obligatoire et. .a  pour. finalité exclusive de votre dossier. Conformement a la | informatique eet libertés | F
mödifiée en 2004. vous béneficiez d'un droit d'acces et de rectification aux  infarmations qui  vous  concernent, que vous pouvez excercer en vous adressant a OPTIQUE LECLERC
RENNES.
Prendre contact avec le médiateur de E.Leclerc
st yous etes en désaccord avec. les solutions apportées par le service cllent et le service Atla E. Leclerc, yous pouvez saisir le médiateur.. E.. Leclerc | appel au  mediateur  du
commerce coopératif et associé. Nous vous rappelons que vous devez passer dans un premier temps par Te 'service, client de Leclerc ainsi que par service Atlo de Leclerc
avant de passer par le mediateur. NVous devez justifier d'une preuve de dépöt E'dey réclämation #écrite et attendre un détai supérieur a trois semaines. | pouvez ess contacter
B3 te biais de Heur: site internet ou un formulaire de contact est votre. disposition.ou t  courrier en écrivant au. .médiateur du Commerce coopératif | associé, FCA, 77 rue
Lourmet. 75015 Paris. Nous  vous rappelons que le service de mediation l'est gratuit |  quil est indépendant. | 1/1
""",
        "output": """
```json
{
"doc_type": "Facture de optique",
"doctor_id": "351771563",
"delivery_add": "6 IMPASSE DES ROCHELLES 35310 SAINT THURIAL",
"billing_add": "",
"security_number": "2 73 06 35 115 060 15",
"insured": "Mme. BEAUVERGER ESTELLE",
"beneficiary": "Mme. BEAUVERGER ESTELLE",
"birthday": "1973/06/18",
"paid_date": "2022/08/23",
"total": "99,40",
}
```"""
    },
    {
        "input": """
CENTALQRR2REALELE6A  RUE JULES VALLES
35065 RENNES
optique | Tél : 0 0223406920
Fax : C 0223406921
E.Leclerc@ | Mail optique.renouest@socamaine.fr
FINESS 352612444
Mme. BEAUVERGER ESTELLE
INom de I'assuré : | M. | 6 IMPASSE DES ROCHELLES
:Numéro tel | 06 44 02 87 62 | 35310 SAINT THURIAL
:Date Naiss. | 18/06/1973
.Caisse
N° sécu Sociale | 2 73 06 35 115 060 15
9900400610003964296 | RENNES, le vendredi 26 aoút 2022
Facture N'F100039642 du 26/08/2022 | FACTURE ACQUITTÉE
Code Produit | Désignation | Prix Unit. Prix Unit. Qté | Montant
Ht (€) | ttC (€) | TTC  | (€)
i00133409 | iBausch \ Lomb Renu 4x360mi | 16,58 | 19,90" | 19,90:
`TVA 20.00
Total HT (€) : | 16,58
Total TTC (€) | 19,90
Net a payer (€) | 19,90
Rêglement
espéce | 19,90
Optique E. LECLERC procede au traitement de YOS données personnelles aux fins.. de : gestion de votre. commande. Les destinataires des. donées sont votre. ..centre | ,gestlon .CPAM et
organisme de complémentaire santé. Cette: collecte | obligatoire et a pour: finalité exctusive de votre dossier. Conformément la roi informatique eet | du .6 janvier 1978
modifiée en 2004, vous bénéficiez d'un droit d'acces | de rectification aux informations qui vous concernent. que vous pouvez excercer en vous adressant a OPTIQUE E. LECLERC
RENNES.
Prendre contact avec le médiateur de E.Leclerc
si  vous etes en désaccord avec les :  solutions apportées par le service client et le service All E. Leclerc, vous pouvez saisir ie mediateur. .E. .Leclerc fait appel au médiateur  du
commerce coopératif et associé. Nous vous rappelons que vous.. devez passer dans un premier temps par le 'service .client de Leclerc ainsi. que par le service. Atla de Leclerc
avant de passer par le médiateur. Vous devez justifier d'une l preuve de dépöt de. réclamation écrite  attendre un délai  supérieur trois  semaines. #Yous pouvez les contacter
par le biais de leur site. internet ou un formulaire de contact est a votre. disposition.ou 1 courrier | écrivant au médiateur du Commerce coopératif et associé. FCA. 77  rue
de Lourmel. 75015 Paris. Nous vous rappelons que le service de médiation est gratuit | quil est i indépendant. | 1/1
""",
        "output": """
```json
{
"doc_type": "Facture de optique",
"doctor_id": "",
"delivery_add": "6 IMPASSE DES ROCHELLES 35310 SAINT THURIAL"
"billing_add": "",
"security_number": "2 73 06 35 115 060 15",
"insured": "Mme. BEAUVERGER ESTELLE",
"beneficiary": "Mme. BEAUVERGER ESTELLE",
"birthday": "1973/06/18",
"paid_date": "2022/08/26",
"total": "19,90",
}
```"""
    },
]


def few_shot_prompt(text):
    process_text = "\n".join(
        f"Human: {example['input']}\nAI: {example['output']}\n"
        for example in text[:3]
    )

    return process_text


few_shot_examples_birthcert_fr = few_shot_prompt(examples_birthcert_fr_str)
few_shot_examples_id_card_vn = few_shot_prompt(examples_id_card_vn_str)
few_shot_examples_receipt_fr = few_shot_prompt(examples_receipt_fr_str)

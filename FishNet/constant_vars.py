###   The internal codes that count by weight(kg)   ###
squid = ["SQ005A", "SQ006A"]
fish = ["S001A", "S003A", "F06", "F91", 'S017A', 'CD001A', 'H006A']
tuna = ['T001A', 'T005A']
lobster = ["L02", "L05", "L06", "L07", "L08", "L86", 'L006A', 'L008A', 'L007A', 'L004A', 'L001A']
crab = ["CR004A", "CR001A", "C18", "C22", 'CR010A']
octopus = ["O21"]
scallop = ["SC001", "SC002", "SC003"]
prawn = ['PV008A', 'PV013A', 'PV015A', 'PV014A', 'PV012A', 'PT002A', 'PT001A']
mussel = ['M001A', 'M003A']
misc = ["O52", 'O003A'] #clam meat, oyster meat

by_kg = squid + fish + tuna + lobster + crab + octopus + scallop + prawn + mussel + misc


###   The entire internal code list   ###
internal_code_list = ['A001', 'AP005', 'AP04', 'AP05', 'AP06', 'AP07', 'B002', 'B003', 'B004', 'B005', 'BAG - PM', 'BAG - TF', 'BAG - ZIP', 'C001', 'C003', 'C005', 'C01', 'C011', 'C014', 'C042', 'C05', 'C06', 'C081', 'C084', 'C086', 'C089', 
'C096', 'C11', 'C13', 'C18', 'C21', 'C22', 'C23', 'C42', 'CD001A', 'CD002', 'CD003', 'CD004', 'CD005', 'CD006', 'CD007', 'CD008', 'CD009', 'CR001A', 'CR003', 'CR004', 'CR004A', 'CR005', 'CR007', 'CR008', 'D001', 'D002', 
'D003', 'D004', 'DK001', 'DK002', 'E001', 'E002', 'ED001', 'ED002', 'EM001', 'EM002', 'F06', 'F09', 'F099', 'F10', 'F101', 'F11', 'F113', 'F116', 'F117', 'F12', 'F121', 'F135', 'F14', 'F15', 'F16', 'F17', 'F176', 'F180', 'F183', 'F184', 'F190', 'F194', 'F21', 'F22', 'F23', 'F248', 'F26', 'F289', 'F313', 'F327', 'F328', 'F333', 'F334', 'F335', 'F336', 'F337', 'F338', 'F339', 'F340', 'F341', 'F342', 'F35', 'F356', 'F360', 'F361', 'F363', 
'F366', 'F369', 'F370', 'F373', 'F374', 'F375', 'F376', 'F43', 'F44', 'F49', 'F54', 'F61', 'F62', 'F84', 'F85', 'F88', 'F89', 'F90', 'F91', 'F92', 'G001', 'G002', 'G004', 'G005', 'G006', 'G008', 'H001', 'H002', 'H003', 'H004', 'HOO5', 'L02', 'L05', 'L06', 'L07', 'L08', 'L081', 'L082', 'L083', 'L084', 'L085', 'L086', 'L087', 'L110', 'L13', 'L130', 'L140', 'L16', 'L160', 'L17', 'L170', 'L183', 'L184', 'L21', 'L85', 'L86', 'M001', 'M002', 
'M003', 'M005', 'M006', 'M011', 'M012', 'M013', 'M014', 'M015', 'M017', 'M018', 'M019', 'M025', 'M026', 'M027', 'M028', 'M029', 'M030', 'M031', 'M035', 'M038', 'M040', 'M041', 'M052', 'M053', 'M060', 'M061', 'M062', 'M063', 'M064', 'M065', 'M066', 'M069', 'M07', 'M070', 'M071', 'M072', 'M073', 'M074', 'M075', 'M106', 'M18', 'M215', 'M26', 'M67', 'M68', 'MS001', 'O002', 'O01', 'O030', 'O05', 'O052', 'O055', 'O060', 'O08', 'O081', 'O082', 'O084', 'O085', 'O088', 'O10', 'O11', 'O110', 'O12', 'O150', 'O21', 'O210', 'O23', 'O30', 'O31', 'O36', 'O37', 'O52', 'O55', 'O81', 'OTHERS', 'OTHERS-SAUCES', 'OY002', 'OY005', 'OY05', 'P001', 'PA001', 'PA003', 'PA004', 'PT001', 'PT002', 'PT004', 'PT006', 'PV003', 'PV004', 'PV006', 'PV008', 'PV014', 'PV015', 'PV016', 'PV017', 'PV018', 'PV019', 'PV020', 'PV021', 'REBATES', 'RENTAL', 'RM020', 'S001', 'S001A', 'S002', 'S003', 'S003A', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S01', 'S010', 'S011', 'S012', 'S013', 'S014', 'S015', 'S017', 'S018', 'S019', 'S020', 'S021', 'S022', 'S023', 'S024', 'S025', 'S026', 'S027', 'S081', 'S082', 'S086', 'S089', 
'S11', 'S13', 'S15', 'S160', 'S161', 'S85', 'S88', 'SA001', 'SA002', 'SA004', 'SA005', 'SA006', 'SB001', 'SC001', 'SC002', 'SC003', 'SC004', 'SC004A', 'SC005', 'SC007', 'SC008', 'SC009', 'SC010', 'SC011', 'SC014', 'SC016', 'SC017', 'SH001', 'SN002', 'SN003', 'SN004', 'SN006', 'SP002', 'SP003', 'SP004', 'SP012', 'SP013', 'SP017', 'SP019', 'SP02', 'SP03', 'SP04', 'SP12', 'SP13', 'SQ001', 'SQ002', 'SQ003', 'SQ004', 'SQ005', 'SQ005A', 'SQ006', 'SQ006A', 'SQ007', 'SW001', 'SW002', 'SW003', 'T001', 'T003', 'T008', 'TF001', 'TF002', 'TP001', 'TP002', 'TP004', 'TP06', 'TP09', 'TP10', 'TV001', 'U001', 'U002', 'VP001', 'VP006', 'VP007', 'VP008', 'VP009', 'VP01', 'VP03', 'VP05', 'VP06', 'VP09', 'VP11', 'VP110', 'VP15', 'VP27', 'VP51']


###   months   ###
months = ["January", "Jan", "February", "Feb", "March", "Mar", "April", "Apr", "May", "June", "Jun", "July", "Jul", "August", "Aug", "September", "Sep", "October", "Oct", "November", "Nov", "December", "Dec"] #we may want to incorporate year? future patch
# i could prob just use datetime for this...


###   i wna cri... from "storebest stocks" excel file   ###
Atka = {
    'A001' : 'Atka Fillet'
    }

Barramundi = {
    'B001': 'Barramundi Fillet', 
    'B002': 'Barramundi Portion 300gm Large', 
    'B003': 'Barramundi Portion 180gm', 
    'B004': 'Barramundi Portion 120gm', 
    'B005': 'Barramundi W/Black Pepper Sauce 200gm', 
    'B006': 'Barramundi Portion 3pkt x 180gm'
    }

Clams = {
    'C001': 'Clam Asari Flower Whole 500gm', 
    'C002A': 'Clam Diamond Whole', 
    'C002': 'Clam Diamond Whole 300gm', 
    'C003': 'Clam Venus Whole 500gm', 
    'C004': 'Clam Meat 400gm', 
    'C005': 'Clam Garlic Butter'
    }

Cod = {
    'CD001A': 'Cod Chilean Seabass Fillet', 
    'CD002': 'Cod Chilean Seabass Portion 500gm', 
    'CD003': 'Cod Chilean Seabass Portion 230gm', 
    'CD004': 'Cod Chilean Seabass Portion 150gm', 
    'CD005': 'Cod Chilean Seabass cube skinless', 
    'CD006': 'Cod Loin Atlantic Skinless 350gm'
    }

Crab = {
    'CR001A': 'Crab King Raw', 
    'CR001': 'Crab King Raw 380gm', 
    'CR002': 'Crab King Cooked 450gm', 
    'CR003': 'Crab Red Meat 320gm (Indonesia)', 
    'CR004A': 'Crab Soft Shell Crab', 
    'CR004': 'Crab Soft Shell Crab 3pcsX100gm', 
    'CR005': 'Crab Handy Soft Shell Crab Tempura', 
    'CR006': 'Crab Handy Meat Tempura', 
    'CR007': 'Crab Snow Leg 250gm', 
    'CR008A': 'Crab Flower Jumbo (Pakistan)', 
    'CR008': 'Crab Flower Jumbo 330gm (Pakistan)', 
    'CR009': 'Crab Cake Handy 3pcs x 3oz', 
    'CR010': 'Crab Meat Eastern Cove Lump'
    }

Crab_meat = {
    'CP061': 'Crab Meat Claw Handy 454GM', 
    'CP062': 'Crab Meat Special Handy 454GM', 
    'CP063': 'Crab Meat Lump Handy 454GM', 
    'CP064': 'Crab Meat Jumbo Lump Handy 454GM', 
    'CP065': 'Crab Meat Colossol Lump Handy 454GM', 
    'CP066': 'Crab Meat Claw Handy 227GM', 
    'CP067': 'Crab Meat Special Handy 227GM', 
    'CP068': 'Crab Meat Lump Handy 227GM', 
    'CP069': 'Crab Meat Jumbo Lump Handy 227GM', 
    'CP070': ''
    }

Dory = {
    'D001': 'Dory Fillet 400gm', 
    'D002': 'Dory Cubes 1kg', 
    'D003': 'Dory Sliced 200gm', 
    'D004': 'Dory Catfish Portion 200gm'
    }

Duck = {
    'DK001': 'Duck Smoked Original 200gm', 
    'DK002': 'Duck Smoked With Pepper 200gm'
    }

Ebi_and_escargot = {
    'E001': 'Ebi Tempura 10 Pcs 250gm (Large)', 
    'E002': 'Ebi Tempura 6 Pcs 270gm (Jumbo)', 
    'E003': 'Escargot 12pcs 89gm'
    }

Emperor_fish = {
    'EM001': 'Emperor Portion 200gm', 
    'EM002': 'Emperor Portion 200gm X 3pcs'
    }

Edamame = {
    'ED001': 'Edamame Original 400gm', 
    'ED002': 'Edamame Salted 400gm'
    }

Grouper = {
    'G001': 'Grouper Portion 300gm Large', 
    'G002': 'Grouper Portion 150gm', 
    'G003': 'Grouper Portion 120gm', 
    'G004': 'Grouper Marble Sliced 300gm', 
    'G005': 'Grouper Red Sliced 300gm', 
    'G006': 'Grouper Red Portion 180-200gm', 
    'G007': 'Grouper Red Portion 300gm', 
    'G008': 'Grouper Portion w/Black Pepper Sauce (250g)'
    }

Halibut = {
    'H001': 'Halibut Fillet 400gm<', 
    'H002': 'Halibut Portion 150gm (skin On) RPC 110569', 
    'H003': 'Halibut Steak 500gm', 
    'H004': 'Halibut Steak Solomon 500gm', 
    'H005': 'Hamachi Portion 150gm', 
    'H006': 'Hamachi Collar 200gm', 
    'H007': 'Hamachi Portion 300gm', 
    'H008': 'Halibut portion Skinless 130g'
    }

Lobster = {
    'L001A': 'Lobster Rock 700gm+- Whole', 
    'L001': 'Lobster Rock 700gm+- Whole', 
    'L002A': 'Lobster Rock 400+- Whole', 
    'L002': 'Lobster Rock 400+- Whole', 
    'L003A': 'Lobster Rock 200+- Whole', 
    'L003': 'Lobster Rock 200+- Whole', 
    'L004A': 'Lobster Rock Tail 300-400gm 10kg', 
    'L004': 'Lobster Rock Tail 340gm', 
    'L005A': 'Lobster Boston Tail 100-200 10kg', 
    'L005': 'Lobster Boston Tail 110gm', 
    'L006A': 'Lobster Boston Cooked Whole 10kg', 
    'L006': 'Lobster Boston Cooked Whole 350gm<', 
    'L007A': 'Lobster Boston Cooked 1/2 cut 10kg', 
    'L007': 'Lobster Boston Cooked 1/2 cut 200gm<', 
    'L008A': 'Lobster Slipper Crayfish Raw 5kg', 
    'L009': 'Lobster Slipper Crayfish Raw 150gm', 
    'L010': 'Crayfish Cooked Original 750gm', 
    'L011': 'Crawfish Cooked In Mala Style 750gm', 
    'L012': 'Crawfish Cooked Garlic Style 750gm', 
    'L013A': 'Lobster Rock 600+ Whole', 
    'L013': 'Lobster Rock 600+ Whole'
    }

Mussel = {
    'M001': 'Mussel Chile Cooked Whole 1kg', 
    'M002': 'Mussel Chile Cooked Whole 500gm', 
    'M003': 'Mussel NZ 1/2 Shell 907gm', 
    'M004': 'Mussel NZ 1/2 Shell 300gm', 
    'M005': 'Mussel Meat 1kg', 
    'M006': 'Mussel Meat 500gm', 
    'M007': 'Mussel Spanish Galican'
    }

Mix_seafood = {
    'MS001': 'Mix Seafood 400gm'
    }

Oyster = {
    'O001': 'Oyster meat 1kg', 
    'O002': 'Oyster Meat 300gm', 
    'O003A': 'Oyster Japan Miyagi whole', 
    'O003': 'Oyster Sashimi whole 1kg', 
    'O004': 'Oyster Breaded 20pcs', 
    'O005': 'Oysters Breaded XL (Boiler)'
    }

Potato_fries = {
    'P001A': 'Potato Sweet Cooked Fries', 
    'P001': 'Potato Sweet Cooked Fries 500gm'
    }

Tiger_prawn = {
    'PT001': 'Prawn Tiger HOSO 8/10 1kg', 
    'PT002': 'Prawn Tiger HOSO 16/20 1kg', 
    'PT003': 'Prawn Tiger HOSO 31/35 1kg', 
    'PT004': 'Prawn Tiger HOSO 3/7 1kg', 
    'PT005': '', 
    'PT006': 'Prawn Tiger PND 8/10 1kg', 
    'PT007': 'Prawn Tiger PND 16/20 1kg', 
    'PT008': 'Prawn Tiger PND 31/40 1kg', 
    'PT009': '', 
    'PT 010': ''
    }

Banana_prawn = {
    'PA001': 'Prawn Ang Kar HOSO 8/10 1kg', 
    'PA002': 'Prawn Ang Kar HOSO 16/20 1kg', 
    'PA003': 'Prawn Ang Kar HOSO 21/30 1kg', 
    'PA004': 'Prawn Ang Kar HOSO 31/40 1kg', 
    'PA005': 'Prawn Ang Kar HOSO 26/30 1kg'
    }

Prawn = {
    'PV001': 'Prawn Vannamei HOSO 8/10 1kg', 
    'PV002': 'Prawn Vannamei HOSO 16/20 1kg', 
    'PV003': 'Prawn Vannamei HOSO 21/25 1kg Sea Prawn', 
    'PV004': 'Prawn Vannamei HOSO 31/40 1kg', 
    'PV005': 'Prawn Vannamei Cooked HOSO 8/10 1kg', 
    'PV006': 'Prawn Vannamei Cooked HOSO 16/20 1kg', 
    'PV007': 'Prawn Vannamei Cooked HOSO 21/25 1kg', 
    'PV008': 'Prawn Vannamei Cooked HOSO 31/35 1kg', 
    'PV009': 'Prawn Vannemei Cooked HOSO Garlic Butter 1kg', 
    'PV010': 'Prawn Vannemei Cooked HOSO 31/40 1kg', 
    'PV011': 'Prawn Vannamei PND 13/15 1kg Jumbo', 
    'PV012': 'Prawn Vannamei PND 16/20 1kg Large', 
    'PV013': 'Prawn Vannamei PND 21/25 1kg', 
    'PV014': 'Prawn Vannamei PND 31/40 1kg Medium', 
    'PV015': 'Prawn Vannamei PND 90/120 1kg Baby', 
    'PV016': 'Prawn Vannamei PND Broken 1kg', 
    'PV017': 'Prawn Vannamei PND 13/15 300gm Jumbo', 
    'PV018': 'Prawn Vannamei PND 16/20 250gm Large', 
    'PV019': 'Prawn Vannamei PND 31/40 250gm Medium', 
    'PV020': 'Prawn Vannamei PND 90/120 250gm Baby', 
    'PV021': 'Prawn Garlic Herb Skewers 200gm (Vietnam)', 
    'PV022': ''
    }

Salmon = {
    'S001A': 'Salmon Fillet Skin -On +-', 
    'S001': 'Salmon Fillet Skin -On +-', 
    'S002': 'Salmon Centre - cut 400gm', 
    'S003A': 'Salmon Trout Fillet Skin-On +-', 
    'S003': 'Salmon Trout Fillet Skin-On +-', 
    'S004': 'Salmon Skinless 200gm (2pcs)', 
    'S005': 'Salmon Burger 200gm', 
    'S006': 'Salmon Sashimi Presliced 100gm', 
    'S007': 'Salmon Hot Smoked Portion 130gm', 
    'S008': 'Salmon Skewer Raw 125gm', 
    'S009': 'Salmon Skewer Teriyaki 125gm', 
    'S010': 'Salmon Portion 150gm', 
    'S011': 'Salmon Portion 3pcs x150gm (450gm)', 
    'S012': 'Salmon Portion 6pcs x 150gm (900gm)', 
    'S013': 'Salmon Portion 9pcs x 150gm (1.35kg)', 
    'S014': 'Salmon Tail cut 150gm', 
    'S015': 'Salmon Belly 200gm', 
    'S016': 'Salmon Smoked Presliced 1kg', 
    'S017': 'Salmon Smoked Presliced 500gm', 
    'S018': 'Salmon Smoked Presliced 100gm', 
    'S019': 'Salmon Smoked Gravlax Presliced 100gm', 
    'S020': 'Salmon King NZ Portion 150gm (New Zealand)', 
    'S021': 'Salmon Alaska Portion 150gm (USA)', 
    'S022': 'Salmon Ikura 250gm', 
    'S023': 'Salmon Ora King Portion 240g (New Zealand)', 
    'S024': 'Salmon Cube 200gm', 
    'S025': 'Salmon Portion With Black Pepper Sauce 280gm', 
    'S026': 'Salmon Smoked Presliced 100gm x 4pkts', 
    'S027': 'Salmon Smoked Gravalax Presliced 100gm x 4pkts', 
    'S028': 'Salmon Skewer 150gm', 
    'S029': 'Salmon Teriyaki Skewer 150gm', 
    'S030': 'Salmon w Napolitan Sauce 250gm', 
    'S031': 'Smoke Salmon 100g x 3pack', 
    'S032': 'Salmon 18 pack (3pcs/pack)',
    'S034': 'Salmon trout 2pc'
    }

Saba = {
    'SA001': 'Saba Mackerel Fillet Raw 3pcs', 
    'SA002': 'Saba Mackerel Fillet Teriyaki 2pcs', 
    'SA003': 'Saba Mackerel Fillet Teriyaki 120gm', 
    'SA004': 'Saba Mackerel Presliced Raw 300gm', 
    'SA005': 'Saba Mackerel Spanish Steak 500gm', 
    'SA006': 'Saba Mackerel Hot Smoked Pepper 100gm'
    }

Seabream = {
    'SB001': 'Seabream Sliced Raw 300gm'
    }

Scallop = {
    'SC001': 'Scallop US U-10 2.27kg/pkt', 
    'SC002': 'Scallop US 10/20 2.27kg/pkt', 
    'SC003': 'Scallop US 20/30 2.27kg/pkt', 
    'SC004A': 'Scallop Bay 1kg', 
    'SC004': 'Scallop Bay 250gm', 
    'SC005': 'Scallop Hokkaido S 1kg', 
    'SC006': 'Scallop Hokkaido M 1kg', 
    'SC007': 'Scallop Hokkaido L 1kg', 
    'SC008': 'Scallop 1/2 shell 1kg', 
    'SC009': 'Scallop Japan 1kg', 
    'SC010': 'Scallop Japan 300gm', 
    'SC011': 'Scallop US 300gm', 
    'SC012': 'Scallop 1/2 Shell 500gm', 
    'SC013': '', 
    'SC014': 'Scallop US Jumbo 500gm', 
    'SC015': 'Scallop US Large 600gm', 
    'SC016': 'Scallop 1/2 shell 500gm', 
    'SC017': 'Scallop W Vemicelli Garlic 500gm'}

Shisamo = {
    'SH001': 'Shisamo 120gm', 
    'SH002': 'Shisamo 150gm'
    }

Soon_hock = {
    'SH003A': 'Soon Hock Whole (Marbled Goby) 300-400gm', 
    'SH003': 'Soon Hock Whole 350gm (Marbled Goby)'
    }

Squid = {
    'SQ001': 'Squid Loligo Whole Large 15/18cm 315gm', 
    'SQ002': 'Squid Loligo Small Cleaned 6/8cm 300gm', 
    'SQ003': 'Squid Octopus leg', 
    'SQ004': 'Squid Baby Octopus 400gm', 
    'SQ005': 'Squid Tube 1kg', 
    'SQ006': 'Squid Ring 1kg', 
    'SQ 007': 'Squid Ring 300gm'
    }

Snapper = {
    'SN001': 'Snapper Portion 150gm', 
    'SN002': 'Snapper Portion 120gm', 
    'SN003': 'Snapper Red Portion 150gm', 
    'SN004': 'Snapper Red Sliced 300gm', 
    'SN006': 'Snapper Red w/Black Pepper Sauce 200gm'
    }

Swordfish = {
    'SW001': 'Swordfish 120gm', 
    'SW002': 'Swordfish 120gm x 3pkts', 
    'SW003': 'Swordfish Belly', 
    'SW004': 'Swordfish Garlic Butter', 
    'SW005': 'Swordfish Cube 200gm'
    }

Threadfin = {
    'TF001': 'Threadfin Portion 150gm', 
    'TF002': 'Threadfin Sliced Raw 300gm'
    }

Travelly = {
    'TV001': 'Trevally Portion 200gm', 
    'TV002': 'Trevally Portion 200gm x 3pcs'
    }

Tilapia = {
    'TP001': 'Tilapia Fillet 1kg', 
    'TP002': 'Tilapia Fillet 500gm'
    }

Unagi = {
    'U001': 'Unagi Jumbo XL 330gm', 
    'U002': 'Unagi Medium 250gm'
    }

Chicken_meat = { #not complete... got internal code changes, im too tired to deal with rn
    'M051': 'Buffalo Wings Spicy', 
    'M052': 'Mooping', 
    'M053': 'Chicken Chop Herb Mix Marinade', 
    'M054': 'Chicken Chop Garlic Honey', 
    'M055': 'Chicken Chop BBQ rub', 
    'M056': 'Chicken Chop Miso Teriyaki', 
    'M057': 'Chicken Chop Chipotle', 
    'M058': 'Chicken Chop Cajun Rub', 
    'M059': 'Chicken Chop Brazlian Mustard', 
    'M060': 'Thai Gai Ping', 
    'M061': 'Tex Mex', 
    'M062': 'Soy Drum Stick'
    }

Soups_and_others = {
    'SP05': 'clam chowder soup', 
    'SP06': 'French Onion Soup', 
    'SP07': 'Hertha Potato & Leek Soup', 
    'SP08': 'Tomato Bisque', 
    'SP09': 'Garlic Purple Sweet Potato', 
    'SP10': 'Sweet garden pea and mint', 
    'SP11': 'Cheese Ball', 
    'SP12': 'Red CRab Clam chowder', 
    'SP13': 'Salmon clam chowder', 
    'SP14': 'Mushroom Noodles', 
    'SP15': 'Taiwanese Noodles', 
    'SP16': 'Char Siew Noodles', 
    'SP17': 'CNY Bundle 2-3 Pax', 
    'SP18': 'CNY Bundle 5-8 pax', 
    'SP19': 'CNY Bundle Hot Pot'
    }

dicts_list = (Atka, Barramundi, Clams, Cod, Crab, Crab_meat, Dory, Duck, Ebi_and_escargot, Emperor_fish, Edamame, Grouper, Halibut, Lobster, Mussel, Mix_seafood, Oyster, Potato_fries, Tiger_prawn, Banana_prawn, Prawn, Salmon, Saba, Seabream, Scallop, Shisamo, Soon_hock, Squid, Snapper, Swordfish, Threadfin, Travelly, Tilapia, Unagi, Chicken_meat, Soups_and_others)
Storebest_stock_dict = {}
for i in dicts_list:
    Storebest_stock_dict.update(i)


###   the madsoft dict is riddled with many copies and old outdated items...   ###
Madsoft_dict = {'A001': 'ATKA FILLET JAPAN', 'AP004': 'PRAWNS ANGKA HOSO 16-20', 'AP005': 'PRAWNS ANGKA HOSO 21/25 ', 'AP006': 'PRAWNS HOSO ANGKA 26/30', 'AP04': 'PRAWNS ANGKA HOSO 16/20', 'AP05': 'PRAWNS ANGKA HOSO 21/25', 'AP07': 'PRAWNS ANGKA HOSO 13/15', 'B001': 'BARRAMUNDI FILLET ', 'B001A': 'BARRAMUNDI FROZEN FILLET', 'B002': 'BARRAMUNDI PORTION LARGE 300G', 'B003': 'BARRAMUNDI PORTION 180G', 'B004': 'BARRAMUNDI PORTION 120G', 'B005': 'BARRAMUNDI-BLK PEPP SAU 200G', 'B006': 'BARRABUMDI PORTION-3PC PACK', 'BAG - PM': 'BAGS PRAWN MEAT 250GR', 'BAG - TF': 'BAGS-TILAPIA FILLET ', 'BAG - ZIP': 'BAGS ZIP ', 'C001': 'CLAMS FLOWER -WHOLE', 'C002': 'CLAMS NZ DIAMOND -300G PACK', 'C003': 'CLAMS VENUS WHITE 500G PACK', 'C004': 'CLAM MEAT 400G', 'C005': 'CLAMS VENUS GARLIC BUTTER SET', 'C01': 'CRAB MEAT CLAW HANDY-454G', 'C04': 'CRAB MEAT J90 JUMBO LUMP HANDY', 'C042': 'CRAB MEAT COLOSSAL-CN', 'C05': 'CRAB MEAT COLOSSAL HANDY 454G', 'C084': 'CRAB LEG KING-270G', 'C085': 'CRAB KING ALASKAN 900G', 'C086': 'CRAB RAW KING CLUSTER-700G', 'C088': 'CRAB SNOW LEG IMT 100G PACK', 'C089': 'CRAB STICK JAP 500G', 'C097': 'CRAB FLOWER SMALL 13PCS 1KG', 'C098': 'CRAB FLOWER LARGE 2PCS 420G', 'C11': 'CRAB MEAT CLAW HANDY-227GM TUB', 'C12': 'CRAB MEAT SPECIAL HANDY-227GM', 'C13': 'CRAB MEAT LUMP HANDY-227G', 'C14': 'CRAB MEAT JUMBOLUMP HANDY-227GM', 'C18': 'CRAB SOFT SHELL 120/150 20', 'C21': 'CRAB SNOW LEG BOILED-250GM', 'C22': 'CRAB SOFT SHELL TEMPURA HANDY', 'C23': 'CRAB CAKE SANTA FE HANDY', 'C42': 'CRAB MEAT COLOSSAL-CN', 'CD001A': 'COD CHILEAN SEABASS FILLET ', 'CD002': 'COD LOIN CTR SKIN ON-500G', 'CD003': 'SEABASS CTR LOIN CHILEAN 230G', 'CD004': 'COD PORTION CHILEAN 150G', 'CD005': 'COD CUBE 200G PACK', 'CD006': 'COD LOIN SKINLESS-350G(2PC)', 'CD007': 'COD BLACK GINDARA 150/200G', 'CD008': 'COD LING FILLET 500G', 'CD009': 'CHILEAN SEABASS BONES', 'CP061': 'CRAB MEAT CLAW HANDY-454GM', 'CP062': 'CRAB MEAT SPECIAL HANDY-454GM', 'CP063': 'CRAB MEAT LUMP HANDY-454GM', 'CP064': 'CRAB MEAT JUMBO LUMP HANDY-454', 'CP065': 'CRAB MEAT COLOSSAL HANDY 30/40', 'CP066': 'CRAB MEAT CLAW HANDY-TUB', 'CP067': 'CRAB MEAT SPECIAL HANDY-TUB', 'CP068': 'CRAB MEAT LUMP HANDY-TUB', 'CP069': 'CRAB MEAT JUMBO LUMP HANDY-TUB', 'CR001': 'CRAB RAW KING LEG 380G', 'CR001A': 'CRAB KING RAW', 'CR002': 'CRAB KING LEG COOKED 450GM', 'CR002A': 'CRAB LEGS KING COOKED', 'CR003': 'CRAB RED MEAT 320G', 'CR004': 'CRAB SOFT SHELL RAW-3PC PACK', 'CR004A': 'CRAB SOFT SHELL 70/100 20', 'CR005': 'CRAB SOFT SHELL TEMPURA-4PCS', 'CR007': 'CRAB SNOW LEG BOILED 250G PK', 'CR008': 'CRAB FLOWER JUMBO 1PC 330G', 'CR009': 'CRAB CAKE HANDY SANTA FE (3PC)', 'CR010': 'CRAB MEAT LUMP EC', 'CR010A': 'CRAB MEAT LUMP-EC', 'D001': 'DORY FILLET -400G', 'D002': 'DORY CUBE 1KG PACK', 'D003': 'DORY SLICES SKINLESS TRAY 300G', 'D004': 'CATFISH SEA CAUGHT 500G', 'DK001': 'DUCK MEAT SMOKED 160-220G', 'DK002': 'DUCK SMOKED BLACK PEPPER 160-220G', 'E001': 'PRAWN TEMPURA 10PCS 250G', 'E002': 'PRAWNS TEMPURA JUMBO 6PC 270G', 'E003': 'ESCARGOTS BURGUNDY FRANCE 12PC', 'ED001': 'EDAMAME (ORIGINAL) 400G', 'ED002': 'EDAMAME (SALTED) X 400G', 'EM001': 'EMPEROR FISH PORTION 200G', 'EM002': 'EMPEROR PORTION 200GX3PC PACK', 'F09': 'SALMON PORTION 400GM PACK', 'F10': 'SALMON FILLET FRESH', 'F101': 'HALIBUT PORTION-3PC PACK', 'F11': 'SALMON PORTION 150G', 'F113': 'SALMON SMOKE 100G', 'F117': 'MACKEREL SMOKE PEPPER 250G PACK', 'F12': 'IKURA 500G PACK', 'F121': 'SABA TERIYAKI 1PC 100G', 'F124': 'SABA MACKERAL FILLET 1PCS', 'F135': 'CATFISH STEAK NW-SKIN ON', 'F14': 'DORY CREAM FILLET', 'F15': 'HALIBUT FILLET 400-600GM', 'F16': 'SALMON PORTION ALASKAN', 'F17': 'SALMON PORTION NZ KING 150/160G', 'F180': 'GROUPER PORTION 150G X3PC PACK', 'F183': 'SNAPPER RED PORTION-3PCS PK', 'F194': 'SNAPPER RED FILLET 500-700G', 'F21': 'COD PORTION-500G PACK', 'F22': 'SALMON SMOKE GRAVLAX PACK 100GM PACK', 'F23': 'SALMON SMOKE TROUT-100GM', 'F248': 'MONKFISH STEW SPICY KOREAN', 'F313': 'SALMON SMOKE PRE-SLICED 500G', 'F327': 'BARRAMUNDI W/GARLIC LEMON SAUCE', 'F33': 'COD LOIN SKINLESS-140/160GM', 'F332': 'SALMON W/HONEY GARLIC', 'F333': 'BARRAMUNDI PORTION W/THAI CITRUS', 'F334': 'CLAMS CHARDONNAY INFUSED ', 'F335': 'SNAPPER W/LEMON BUTTER', 'F336': 'PRAWNS HOSO SEA TIGER COLL U3 SZ 4-6 500G ', 'F337': 'PRAWNS HOSO SEA TIGER U5 6-8 500G ', 'F338': 'PRAWNS HOSO WILD TIGER XL 6-8 500G ', 'F339': 'PRAWNS HOSO WILD TIGER XL 11-13 500G', 'F340': 'PRAWNS HOSO BANANA 21-30 500G ', 'F341': 'PRAWNS MEAT BANANA TAIL ON SZ 20-30 500G', 'F342': 'PRAWNS HOSO BANANA MEDIUM 1KG', 'F35': 'SALMON SASHIMI SLICES 100G PK', 'F356': 'TOMAN SLICES 200G PACK', 'F374': 'ROE LUMPFISH (NORWAY) 100G', 'F39': 'SWORDFISH STEAK', 'F43': 'BARRAMUNDI PORTION 180/220G', 'F44': 'HALIBUT STEAK BONE IN 500G PACK', 'F46': 'SALMON SATAY ORIGINAL', 'F47': 'SALMON SATAY TERIYAKI', 'F49': 'TELIPIA SKINLESS', 'F54': 'MACKEREL TERIYAKI-100G PK', 'F61': 'COD CUBE 200G', 'F62': 'COD LING FILLET-500G PACK', 'F84': 'UNAGI JUMBO SZ 300G PACK', 'F85': 'UNAGI 200GM PACK ', 'F90': 'SQUID LOLIGO WHOLE 6-8 300G TRAY', 'F91': 'SALMON BELLY 2PC PACK', 'G001': 'GROUPER PORTION 350-400G', 'G002': 'GROUPER PORTION 150G', 'G003': 'GROUPER PORTION 120GM', 'G004': 'GROUPER MARBLE SLICES 300G TRAY', 'G005': 'GROUPER RED SLICED 300G PACK', 'G006': 'GROUPER PORTION RED 180G', 'G007': 'GROUPER RED PORTION 300GM', 'G008': 'GROUPER PORTION W/BLACK PEPPER SAUCE (250G)', 'H001': 'HALIBUT FILLET 500-600GM', 'H002': 'HALIBUT PORTION 150G', 'H003': 'HALIBUT STEAK ATLANTIC-500G PACK', 'H004': 'HALIBUT STEAK SALOMON SEA 500G', 'H005': 'HAMACHI PORTION 150G', 'H006': 'HAMACHI COLLAR ', 'H006A': 'HAMACHI COLLAR', 'H007': 'HAMACHI PORTION 300G', 'H008': 'HALIBUT PORTION SKINLESS 130G', 'L001': 'LOBSTER RAW 7/8', 'L001A': 'LOBSTER RAW 7/8', 'L002': 'LOBSTER RAW 3/4', 'L002A': 'LOBSTER RAW 3/4', 'L003': 'LOBSTER ROCK WHOLE 200/300GM ', 'L003A': 'LOBSTER ROCK 2/3', 'L004': 'LOBSTER ROCK TAIL 300G', 'L004A': 'LOBSTER ROCK TAIL 300G', 'L005': 'LOBSTER TAIL BOSTON 150G', 'L005A': 'LOBSTER TAIL BOSTON', 'L006': 'LOBSTER BOSTON COOKED WHOLE', 'L006A': 'LOBSTER COOKED BOSTON 350/400GM', 'L007': 'LOBSTER BOSTON COOKED 1/2 CUT ', 'L007A': 'LOBSTER 1/2 CUT BOSTON COOKED  BOSTON ', 'L008A': 'LOBSTER SLIPPER', 'L009': 'LOBSTER SLIPPER', 'L010': 'CRAWFISH COOKED 4-6 ', 'L011': 'CRAWFISH COOKED MALA 750G', 'L012': 'CRAWFISH COOKED GARLIC 750G', 'L013': 'LOBSTER ROCK WHOLE 600GM', 'L013A': 'LOBSTER ROCK WHOLE 600GMUP', 'L082': 'LOBTSER RAW 2/3', 'L11': 'LOBSTER BAMBOO WHOLE 150-200G', 'L110': 'LOBSTER BABY 2PC (300G)', 'L125': 'LOBSTERS ROCK BABY 800G', 'L13': 'CRAWFISH COOKED 4-6', 'L16': 'CRAWFISH COOKED MALA 750G', 'L17': 'CRAWFISH COOKED GARLIC 750G', 'L183': 'LOBSTER WHOLE COOKED-3PCS', 'L184': 'LOBSTER BOSTON COOKED 1/2 CUT-3 PC PACK', 'L85': 'LOBSTER TAIL BAMBOO 200GUP', 'M001': 'MUSSELS WHOLE CHILEAN 1KG', 'M001A': 'MUSSELS WHOLE CHILEAN 1KG', 'M002': 'MUSSELS BLUE COOKED 500G', 'M003': 'MUSSELS 1/2 SHELL  NEW ZEALAND 907G BOX', 'M003A': 'MUSSELS 1/2 SHELL NEW ZEALAND 907GM BOX', 'M004': 'MUSSELS NZ 1/2 SHELL -300G', 'M005': 'MUSSEL MEAT 1KG', 'M006': 'MUSSEL MEAT 500G PACK', 'M011': 'DUCK CONFIT LEG 2PCS', 'M012': 'CHICKEN THIGH ORIENTAL TANGY 220G', 'M013': 'CHICKEN BREAST HICKORY 220G', 'M014': 'CHICKEN LEG VIET LEMONGRASS 220G', 'M015': 'CHICKEN BREAST KOR GOUCHUJANG  220G', 'M016': 'CHICKEN LEG SALSA VERDE 220G', 'M017': 'CHICKEN THIGH THAI GAIYANG', 'M018': 'CHICKEN THIGH TANDOOR MASALA', 'M019': 'CHICKEN THIGH BALINESE 220G', 'M021': 'CHICKEN CRISPY  W/SEAWEED 1KG', 'M024': 'CHICKEN CRISPY STICK 1KG', 'M025': 'CHICKEN SKEWERS SICHUAN MALA 6STICKS', 'M026': 'CHICKEN SKEWERS BALINESE 6STICKS', 'M027': 'CHICKEN SKEWERS FRENCH BROCHETTES 6STICKS', 'M028': 'CHICKEN SKEWERS KOREAN GOUCHUJANG 6STICKS', 'M029': 'CHICKEN SKEWERS SMK TERIYAKI 6STICKS', 'M030': 'CHICKEN SKEWERS MALAYAN RENDANG 6STICKS', 'M031': 'CHICKEN SKEWERS TIKKA MASALA 6STICKS', 'M035': 'LAMB SKEWERS BEIJING INSPIRED 6STICKS', 'M038': 'PORK BELLY BEIJING INSPIRED SKEWERS 6STICKS', 'M040': 'BEEF SKEWERS BEIJING INSPIRED 6STICKS', 'M041': 'BEEF SKEWERS TURKISH-6 STICKS', 'M045': 'BEEF A4 WAGYU RIBEYE STEAK CUT 200G', 'M052': 'MOOPING THAI 250G', 'M053': 'GAIPING THAI 250G', 'M060': 'CHICKEN LEG (MIXED HERBS)', 'M061': 'CHICKEN LEG (HONEY SOY BLK PEPPER)', 'M062': 'CHICKEN LEG (BBQ)', 'M063': 'CHICKEN LEG (MISO TERIYAKI)', 'M064': 'CHICKEN LEG (CHIPOLTE)', 'M065': 'CHICKEN LEG (CAJUN)', 'M066': 'CHICKEN LEG (BRAZILIAN MUSTARD)', 'M069': 'MIDWINGS BBQ RUB 300G', 'M07': 'BEEF KAGOSHIMA WAGYU A4-TENDERLOIN', 'M070': 'MIDWINGS MIXED HERB RUB', 'M071': 'MIDWINGS MISO TERIYAKI 300G', 'M072': 'DRUMSTICK SOY BRAISED', 'M073': 'LAMB SHORT RIB 400G', 'M074': 'CHICKEN CHOP BLACK PEPPER HONEY ', 'M075': 'CHICKEN CHOP SPICY THAI BASIL ', 'M106': 'CHICKEN CAJUN MARINATED', 'M11': 'CHICKEN BREAST LOUSIANA', 'M12': 'CHICKEN THIGH ORIENTAL TANGY', 'M15': 'CHICKEN BREAST KOR GOUCHUJANG ', 'M16': 'CHICKEN THIGH SALSA VERDE', 'M17': 'CHICKEN LEG THAI GAI YANG ', 'M18': 'CHICKEN LEG TANDOOR MASALA ', 'M19': 'CHICKEN LEG BALI SPICE', 'M21': 'CHIC CRISPY SEAWEED-1 KG P', 'M215': 'CHICKEN BREAST KOREAN GOCHUJANG 2PC PACK', 'M24': 'CHICKEN STICK CRISPY', 'M26': 'BALINIESE SPICE CHIX SKEWERS', 'M29': 'CHICKEN SKEWERS SMOKY TERIYAKI 6 STICKS', 'M35': 'LAMB SKEWERS BEIJING INSPIRED 6STICKS', 'M45': 'BEEF A4 WAGYU RIBEYE STK CUT 200G', 'M67': 'DUCK MEAT SMOKED 160-220G', 'M68': 'DUCK MEAT SMOKED BLK PEPPER 160-220G', 'MS001': 'SEAFOOD MIX BAG 400G', 'MS002': 'SEAFOOD MIXED HOT POT COMBO 400G TRAY', 'O001': 'OYSTER MEAT', 'O002': 'OYSTERS MEAT 280G PACK', 'O003': 'OYSTERS WHOLE JAPAN MIYAGI 1KG PACK', 'O003A': 'OYSTERS WHOLE JAPAN MIYAGI 10-13', 'O004': 'OYSTERS BREADED TRAY', 'O005': 'OYSTERS BREADED XL', 'O05': 'CLAMS FLOWER COOKED 20-30 500G PACK', 'O052': 'CLAM MEAT 500G', 'O058': 'MAKI SUSHI STICK ', 'O086': 'MUSSELS 1/2 SHELL 800G AFRICA', 'O10': 'MUSSEL MEAT COOKED 1KG PACK', 'O11': 'CLAMS WHITE VENUS  500G PACK', 'O12': 'MUSSELS BLUE COOKED 500G PACK', 'O150': 'TRUFFLE OIL WHITE 250ML', 'O21': 'OCTOPUS SQUID LEGS 200G', 'O210': 'OCTOPUS SQUID LEG 200G PACK', 'O24': 'OYSTERS BREADED XL', 'O240': 'SQUID WHOLE SPICY', 'O30': 'OSYTERS BREADED-20PCS TRAY', 'O36': 'EDAMAME (ORIGINAL)', 'O37': 'EDAMAME (SALTED)', 'O52': 'CLAM MEAT', 'O53': 'MUSSEL MEAT BLUE', 'O55': 'CLAM MEAT 400G PACK', 'O81': 'MUSSELS 1/2 SHELL NZ COOKED -300G', 'OTHERS': 'OTHERS', 'OTHERS-SAUCES': 'NAPOLITA SAUCE', 'OY005': 'OYSTERS WHOLE JAPAN MIYAGI 10-13', 'P001': 'SWEET POTATO STICK 500G', 'P001A': 'SWEET POTATO FRIES-1 KG PACK', 'PA001': 'PRAWNS ANGKA HOSO 8-10', 'PA001A': 'PRAWNS ANGKA HOSO 8/10', 'PA002': 'PRAWN ANG KAR HOSO 16/20 1KG ', 'PA003': 'PRAWNS ANGKA HOSO 21/30', 'PA004': 'PRAWNS ANGKA HOSO 30/40', 'PA005': 'PRAWNS ANGKA HOSO 26/30', 'PT001': 'PRAWNS TIGER HOSO JUMBO 8/10', 'PT001A': 'PRAWNS TIGER HOSO(8/10) ', 'PT002': 'PRAWNS TIGER HOSO 16/20', 'PT002A': 'PRAWNS TIGER HOSO 16-20', 'PT003': 'PRAWNS TIGER HOSO 31/35', 'PT004': 'PRAWN TIGER HOSO 3-7 1KG', 'PT005': 'PRAWNS HOSO TIGER (13/15)', 'PT006': 'PRAWN TIGER MEAT GIANT 1KG', 'PT007': 'PRAWN TIGER MEAT 16-20 1KG', 'PT008': 'PRAWN TIGER MEAT 31/40 1KG', 'PV001': 'PRAWN VANNAMEI HOSO 8/10 1KG', 'PV002': 'PRAWN VANNAMEI HOSO 16/20 1KG', 'PV003': 'PRAWNS VANNAMEI HOSO 21/25 SEA 1KG PACK', 'PV004': 'PRAWNS VANAMEI HOSO 31/40', 'PV005': 'PRAWN VANNAMEI COOKED HOSO 8/10 1KG', 'PV006': 'PRAWN HOSO COOKED VANNAMEI 16/20', 'PV007': 'PRAWN VANNAMEI COOKED HOSO 21/25 1KG', 'PV008': 'PRAWNS HOSO COOKED 31/35 ', 'PV008A': 'PRAWN HOSO COOKED VANAMEI 31/35', 'PV009': 'PRAWN COOKED LG  GARLIC BUTTER SET', 'PV010': 'PRAWNS VANNAMEI COOKED HOSO 31/40 1KG', 'PV011': 'PRAWN MEAT JUMBO 13/15', 'PV012': 'PRAWN MEAT JUMBO 16-20 1KG', 'PV012A': 'PRAWN MEAT VANNAMEI 16/20 1KG', 'PV013': 'PRAWN MEAT SZ (L) 1KG 21/25', 'PV013A': 'PRAWN MEAT VANAMEI LARGE', 'PV014': 'PRAWNS MEAT NAKED 31/40 1KG', 'PV014A': 'PRAWN MEAT VANAMEI MEDIUM 1KG', 'PV015': 'PRAWN MEAT BABY 1KG', 'PV015A': 'PRAWN MEAT VANAMEI BABY ', 'PV016': 'PRAWN VANNAMEI BROKEN MEAT 1KG', 'PV016A': 'PRAWN MEAT BROKEN ', 'PV017': 'PRAWN MEAT VANAMEI JUMBO 300G', 'PV018': 'PRAWN MEAT VANAMEI  LARGE-250G', 'PV019': 'PRAWN MEAT VANAME MEDIUM -250G', 'PV020': 'PRAWN MEAT BABY 250G', 'PV021': 'SHRIMP SKEWERS GARLIC HERBS', 'REBATES': 'REBATES', 'RENTAL': 'RENTAL', 'RM020': 'OCTOPUS GOUCHUJANG STEW', 'RM021': 'SEAFOOD STEW SPICY', 'RM025': 'CORN DOG MOZARELLA ', 'RM026': 'CORN DOG CHEDDAR MOZZ ', 'RP03': 'PRAWNS WHOLE CARABINERO 28/34', 'S001': 'SALMON FILLET 1.3KG UP', 'S001A': 'SALMON FILLET 1.3KG UP', 'S002': 'SALMON PORTION CUT 400G', 'S003': 'TROUT FILLET', 'S003A': 'SALMON TROUT FILLET', 'S004': 'SALMON PORTION SKINLESS 2PC', 'S005': 'SALMON BURGER', 'S006': 'SALMON SASHIMI SLICES 100G', 'S007': 'SALMON HOT SMOKE 130G', 'S008': 'SALMON SATAY ORIGINAL', 'S009': 'SALMON TERIYAKI SATAY', 'S010': 'SALMON PORTION CUT-150G', 'S011': 'SALMON PORTION 150GX3PCS', 'S012': 'SALMON PORTION 150G X 6PCS', 'S013': 'SALMON PORTION-150G X 9PCS', 'S014': 'SALMON TAIL CUT', 'S015': 'SALMON BELLY 250G', 'S016': 'SALMON SMOKED PRESLICED 1KG', 'S017': 'SALMON SMOKE PRESLICED-500G PACK', 'S017A': 'SALMON SMOKE 500G PACK', 'S018': 'SALMON SMOKE PRESLICED 100G NW', 'S019': 'SALMON SMOKE GRAVLAX 100G SN', 'S020': 'SALMON NZ KING  PORTION 150G', 'S021': 'SALMON PORTION ALASKAN-170G', 'S022': 'SALMON ROE (IKURA) 250G', 'S023': 'SALMON ORA KING NZ 240G', 'S024': 'SALMON POKE CUBES-250G', 'S025': 'SALMON W BLK PEPPER SAUCE', 'S026': ' SALMON SMOKE 100GX4PKTS FESTIVE PACK ', 'S027': 'SALMON GRAVLAX 4PC-400G', 'S030': 'SALMON W/NAPOLITANA HERBS SAUCE', 'S031': 'SALMON SMOKED 100GX3PACKS', 'S032': 'SALMON PORTION 150GX3PCSX18PKTS', 'S034': 'SALMON TROUT 2PC', 'S081': 'SCALLOPS JUMBO 1/2 SHELL-1KG', 'S082': 'SCALLOPS HOKKAIDO-500G', 'S083': 'SCALLOPS JUMBO 1/2 SHELL 500G', 'S11': 'SCALLOPS JAP 1/2 SHELL (7-8CM)', 'S15': 'SCALLOPS GARLIC  WITH VERMICELLI', 'S161': 'ESCARGOTS BURGUNDY FRANCE 48PC', 'S85': 'SCALLOPS JAPAN 300G PACK', 'S88': 'SCALLOPS USA 300G', 'SA001': 'SABA MACKEREL FILLET X3PCS', 'SA002': 'SABA FILLET TERIYAKI-2PCS PACK', 'SA003': 'MACKERAL TERIYAKI NORWEIGIAN 100G', 'SA004': 'MACKERAL SLICES 300G TRAY', 'SA005': 'MACKEREL-BATANG STEAK 500G', 'SA006': 'MACKEREL HOT SMK PEPPER 100G', 'SB001': 'SEABREAM SLICES 300G TRAY', 'SC001': 'SCALLOPS JUMBO U-10', 'SC002': 'SCALLOP USA 10/20', 'SC003': 'SCALLOPS USA 20/30', 'SC004': 'SCALLOPS BAY 250G', 'SC004A': 'SCALLOPS BAY 80/100', 'SC005': 'SCALLOPS HOKKAIDO 1KG BOX', 'SC005A': 'SCALLOP HOKKAIDO SZ S (31-35)', 'SC006': 'SCALLOPS HOKKAIDO M 1KG BOX', 'SC006A': 'SCALLOPS HOKKAIDO M 1KG BOX', 'SC007': 'SCALLOP HOKKAIDO SZL', 'SC008': 'SCALLOPS 1/2 SHELL -1KG S', 'SC009': 'SCALLOPS YOROKOBI JAPAN 1KG', 'SC010': 'SCALLOP 30/40 JAPAN -300G', 'SC011': 'SCALLOPS USA  (L)-300G PACK', 'SC011/A': 'SCALLOP JAPAN 30/40', 'SC012': 'SCALLOPS 1/2 SHELL -500G S', 'SC014': 'SCALLOPS JUMBO  500G', 'SC015': 'SCALLOP (L) USA-600G', 'SC016': 'SCALLOPS USA L-907G', 'SC017': 'SCALLOP WITH GARLIC VERMICELLI', 'SH001': 'SHISHAMO 120G', 'SH002': 'SHISHAMO 150GM', 'SH003': 'GOBY MARBLE 300-400G', 'SH003A': 'GOBY MARBLE WHOLE', 'SN001': 'SNAPPER PORTION 150GM', 'SN002': 'SNAPPER PORTION 120G', 'SN003': 'SNAPPER RED PORTION 150G', 'SN004': 'SNAPPER RED SLICED 300G', 'SN006': 'SNAPPER RED-BLK PEPP SAU 200G', 'SP001': 'CLAMS SOUP 500G', 'SP002': 'CHOWDER BOSTON CLAM ', 'SP003': 'CHOWDER FRENCH TRUFFLE MUSHROOM ', 'SP004': 'CHOWDER BRITISH PUMPKIN ', 'SP012': 'CHOWDER RED CRAB CLAM ', 'SP013': 'CHOWDER SMOKE SALMON ', 'SP017': 'CNY ABUNDALE BUNDLE 2-3 PAX', 'SP019': 'CNY ABUNDANCE HOT POT (3-4PAX) 2KG', 'SP02': 'CHOWDER BOSTON CLAM ', 'SP03': 'CHOWDER TRUFFLE MUSHROOM ', 'SP04': 'CHOWDER PUMPKIN CARROT ', 'SP12': 'CHOWDER RED CRAB ', 'SP13': 'CHOWDER SALMON SMOKE', 'SQ001': 'SQUID WHOLE 2PC PACK', 'SQ002': 'SQUID BABY CLEANED HEADONS 300G TRAY', 'SQ003': 'OCTOPUS LEG JUMBO 380G', 'SQ004': 'OCTOPUS BABY WHOLE 400G', 'SQ005': 'SQUID TUBE 1KG PACK', 'SQ005A': 'SQUID TUBE 1KG PACK', 'SQ006': 'SQUID RING 1KG PACK', 'SQ006A': 'SQUID RING 1KG PACK', 'SQ007': 'SQUID RING 300G', 'SQ008': 'SQUID TUBE 500G', 'SW001': 'SWORD FISH STEAK 1 PC', 'SW002': 'SWORD FISH STEAK-3PCS', 'SW003': 'SWORDFISH BELLY 230G  ( NON SASHIMI )', 'SW004': 'SWORDFISH STEAK GARLIC BUTTER FESTIVE SET', 'SW005': 'SWORDFISH CUBE 200G', 'T001': 'TUNA STEAK SAKU-450G', 'T001A': 'TUNA SAKU 400-600G', 'T002': 'TUNA SAKU PORTION', 'T002A': 'TUNA SAKU 200-300G', 'T003': 'TUNA SAKU -150G', 'T004': 'TUNA STEAK 150G X 3PCS', 'T005': 'TUNA CUBE MINI 500G PACK', 'T005A': 'TUNA CUBE MINI 500G PACK', 'T006': 'TUNA SAKU CUBES 500GM UNSHAPE', 'T007': 'TUNA STEAK MINI 350G PACK', 'T008': 'TUNA BELLY ( NON SASHIMI ) ', 'T009': 'TUNA CUBE 300G TRAY', 'T010': 'TUNA COLLAR 350G', 'TF001': 'THREADFIN PORTION 150/180G', 'TF002': 'THREADFIN SLICES 300G TRAY', 'TP001': 'TELIPIA FILLET-1KG', 'TP002': 'TILIPIA FILLET-500G', 'TP004': 'PRAWNS HOSO COLOSOL JUMBO  1KG', 'TV001': 'TREVALLY PORTION 200G PACK', 'TV002': 'TREVALLY PORTION 200GX3PCS', 'U001': 'UNAGI JUMBO SIZE 300G PACK', 'U002': 'UNAGI 50V 190-200G JAP(S)', 'VP008': 'PRAWNS HOSO COOKED 16/20 LARGE', 'VP009': 'PRAWNS HOSO MEDIUM 21/25', 'VP05': 'PRAWN HOSO VANAMEI 21/25', 'VP09': 'PRAWN HOSO VANAMEI 26/30', 'VP11': 'PRAWN MEAT COOKED 31/40', 'VP110': 'PRAWN MEAT COOKED 1KG', 'VP27': 'PRAWNS HOSO COOKED 26/30'}



###   For picking   ###
Freezer_1 = ('T003', 'T007', 'SH001', 'SA002', 'SA003', 'SA001', 'TF001', 'D001', 'D002', 'F289')
Freezer_2_and_3 = ('SC004', 'O002', 'SC012', 'M006', 'SC011', 'M002', 'S088', 'M001', 'SC009', 'SQ004', 'SC010', 'O110', 'O085', 'M004', 'SC015', 'SC014')
Freezer_3_half = ('SP003', 'SP002')
Freezer_4 = ('B002', 'G002', 'G006', 'B004', 'H005', 'CD008', 'SN002', 'G007', 'F099', 'B003')
Freezer_5 = ('SQ001', 'SQ002', 'E002', 'E001', 'F126', 'SQ006', 'CD003', 'SW001', 'CD006')
Freezer_6 = ('S011', 'S012', 'S013', 'S002', 'S017', 'S003', 'S024', 'S001', 'S019', 'S027')
Freezer_7 = ('M003', 'VP010', 'PA004', 'TP006', 'TP004', 'PA003', 'L010', 'L011', 'L010')

Freezer_8 = (
    'CD007',
    'CR004', 'TP002', 
    'CR007', 'O003', 
    'C004', 'S034', 
    'ED001', 'U001', 
    'ED002', 'U002'
    )
Freezer_9 = (
    'L009', 'S090', 
    'S026', 'TP001', 
    'L002', 'H006', 
    'L001', 'L006', 
    'T009', 'L007'
    )
Freezer_10 = (
    'CR008', 'S025', 
    'S020', 'S014', 
    'S021', 'S015', 
    'S010', 'S018', 
    'S004', 'MS001', 
    'L005', 'T001'
    )
Freezer_11 = (
    'F328', 
    'CD004', 'SQ005', 
    'CD002', 'C096', 
    'CD005', 'CR002',
    'SQ007', 'SA005', 
    'PV021', 'S082'
    )
Freezer_12 = (
    'F347',
    'PV020', 'PV015',
    'PV019', 'PV014',
    'PV018', 'PV012',
    'PV017', 'PV011',
    'H001', 'PV016'
    )

Slices = (
    'D003', 'DK002',
    'DK001',
    'TF002', 'G005',
    'F356', 'G004',
    'SB001', 'S022',
    'SA004'
)

Chicken = (
    'T008', 'SP012', 'M030', 'M026', 'M031', 'M026', 'M029',
    'M053', 'M018', 'M019', 
    'S007', 'M035', 'S008', 'S009',
    'M071', 'M075', 'M062', 'M060', 'M071',
    'M072', 'M074', 'M069', 'M073',
    'M063', 'SP004', 'SP013',
    'F135'
)

For_picking = {
    'Freezer_1': Freezer_1, 
    'Freezer_2_and_3': Freezer_2_and_3, 
    'Freezer_3_half': Freezer_3_half, 
    'Freezer_4': Freezer_4, 
    'Freezer_5': Freezer_5, 
    'Freezer_6': Freezer_6, 
    'Freezer_7': Freezer_7, 
    'Freezer_8': Freezer_8,
    'Freezer_9': Freezer_9, 
    'Freezer_10': Freezer_10, 
    'Freezer_11': Freezer_11, 
    'Freezer_12': Freezer_12, 
    'Slices': Slices, 
    'Chicken': Chicken}
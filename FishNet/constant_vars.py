###   The internal codes that count by weight(kg)   ###
squid = ["SQ005A", "SQ006A"]
fish = ["S001A", "S003A", "F06", "F91"]
lobster = ["L02", "L05", "L06", "L07", "L08", "L86"]
crab = ["CR004A", "CR001A", "C18", "C22"]
octopus = ["O21"]
scallop = ["SC001", "SC002", "SC003"]
misc = ["O52"] #clam meat

by_kg = squid + fish + lobster + crab + octopus + scallop + misc


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


###   i wna cri   ###
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
    'S032': 'Salmon 18 pack (3pcs/pack)'
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
Internal_dict = {}
for i in dicts_list:
    Internal_dict.update(i)

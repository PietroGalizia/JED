# Jörmungandr's Elemental Diets: The World Snake

from tkinter import *
import random

# Define the elements
elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

#Define diets
Diets_list = [
    "elements of life", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    "critical raw elements", #Document 52020DC0474
    "elements of a smartphone", #Figure 10 of https://doi.org/10.1016/j.jclepro.2023.138099
    "elements of DNA", #https://edu.rsc.org/feature/elements-of-life/3007327.article
    "radioactive elements (U-Th decay series)", #Table 2 of https://doi.org/10.1016/B978-0-08-095975-7.00906-2
    "elements considered safety (grades A-E)\n in the first wall of fusion power plan", #Figure 8 of https://doi.org/10.13182/FST19-1-146
    "elements dedicated to scientists", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elements with names of latin derivation", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elements with names of greek derivation", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elements with names derived from cities, \ncountries, or elsewhere", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elements with names not derived from latin or greek, \nnor from cities or countries", #http://www.liceorodolico.it/appunti/lim/IVF/SCIENZE/I%20nomi%20degli%20elementi%20e%20la%20loro%20origine-tottola%20biennio.pdf
    "elements in solid state at standard temperature and pressure", # https://ptable.com/?lang=it#Propriet%C3%A0
    "elements in liquid state at standard temperature and pressure", # https://ptable.com/?lang=it#Propriet%C3%A0"solid elements at (choose the temperature) °C", # Check the elements on PTABLE: https://ptable.com/?lang=it#Propriet%C3%A0
    "elements in gas state at standard temperature and pressure", # https://ptable.com/?lang=it#Propriet%C3%A0"liquid elements at (choose the temperature) °C", # Check the elements on PTABLE: https://ptable.com/?lang=it#Propriet%C3%A0
    #"gas elements at (choose the temperature) °C", # Check the elements on PTABLE: https://ptable.com/?lang=it#Propriet%C3%A0
    #"elements that melt at (choose the temperature) °C", # Check the elements on PTABLE: https://ptable.com/?lang=it#Propriet%C3%A0
    "metals",
    "nonmetals",
    "elements of group I (Hydrogen & alkali metals)",
    "elements of group II (Alkaline earth metals)",
    "elements of group XV (Pnictogens)",
    "elements of group XVI (Chalcogens)",
    "elements of group XVII (Halogens)",
    "elements of group XVIII (Noblegases)",
    "lanthanides",
    "actinides",
    "transition metals",
    "post-transition metals",
    "metalloids",
    "reactive nonmetals",
    "s-block elements",
    "p-block elements",
    "d-block elements",
    "f-block elemnts",
    #"earth elements", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    #"elements of the Earth's crust", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    #"elements of the Earth's mantle", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    #"elements of the Earth's core", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    #"elements of the oceans", #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
    #"elements of the atmosphere" #Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971
]

Elements_of_Diet = [
    ["O", "C", "H", "N", "P", "Ca", "S", "K", "Na", "Cl", "Mg", "Fe", "Zn", "Cr", "Co", "Cu", "Mn", "Mo", "Ni", "V", "Si", "B", "Se", "F", "I", "Br"],
    ["Sb", "Ba", "Al", "Be", "Bi", "B", "Co", "F", "Ga", "Ge", "Hf", "In", "Li", "Mg","Nb","P", "Sc","Si","Sr","Ta","Ti","W","V"],
    ["Cu", "Al", "Ba", "Ni", "Ca", "Sn", "Fe", "Zn", "Ti", "Pb", "Ag", "Sr", "Au", "Mn", "Zr", "B", "Mg", "U", "Na", "W", "Cr", "Te", "Ge", "Ta", "Pd", "Nb", "Bi", "Ir", "Pt", "Li", "Y", "V", "Hf", "Be", "As", "In", "K", "Ga", "Co", "Sb", "Mo", "Sc", "Cd", "Re"],
    ["C", "H", "O", "N", "P"],
    ["U", "Th", "Pa", "Ra", "Rn", "Po", "Pb", "Bi", "Pu", "Ac", "Tl", "Am", "Np"],
    ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Mg", "Al", "Si", "P", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Fe", "Co", "Ni", "Cu", "Ge", "Se", "Kr", "Sr", "Y", "Ru", "Sn", "Te", "I", "Xe", "Cs", "Ba", "Ce", "Nd", "Sm", "Dy", "Yb", "Lu", "Tl"],
    ["Ge", "Sm", "Gd", "Bi", "Cm", "Es", "Fm", "Md", "No", "Lr", "Rf", "Sg", "Bh", "Mt", "Rg", "Og"],
    ["B", "C", "F", "Na", "Al", "Si", "S", "K", "Ca", "Sc", "Mn", "Fe", "Cu", "Ga", "Ge", "Rb", "Ru", "Pd", "In", "Sn", "Sb", "Te", "Cs", "La", "Ce", "Pm", "Eu", "Ho", "Tm", "Lu", "Hf", "Ta", "Ir", "Au", "Hg", "Pb", "Bi", "Po", "Rn", "Ra", "Np", "Cm", "Hs"],
    ["H", "He", "Li", "Be", "N", "O", "Ne", "P", "Cl", "Ar", "Ti", "Cr", "Co", "As", "Se", "Br", "Kr", "Nb", "Mo", "Tc", "Rh", "Ag", "Cd", "Sb", "I", "Xe", "Ba", "La", "Pr", "Nd", "Dy", "Os", "Tl", "Bi", "At", "Ac", "Pa", "U", "Pu"],
    ["Mg", "Sc", "Mn", "Ga", "Ge", "Se", "Sr", "Y", "Nb", "Tc", "Ru", "Pd", "Cd", "Te", "Eu", "Tb", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Re", "Bi", "Po", "Fr", "U", "Np", "Am", "Bk", "Cf", "Db", "Hs", "Ds"],
    ["V", "Ni", "Zn", "Zr", "Sb", "W", "Pt", "Th"],
    ["Li", "Be", "B", "C", "Na", "Mg", "Al", "Si", "P", "S",  "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Tl", "Pb", "Bi", "Po", "At", "Fr", "Ra", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"],
    ["Hg", "Br"],
    ["H", "He", "N", "O", "F", "Ne","Cl", "Ar", "Kr", "Xe", "Rn"],
    ["Li", "Be", "Na", "Mg", "Al", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"],
    ["H", "He", "B", "C", "N", "O", "F", "Ne", "Si", "P", "S", "Cl", "Ar", "Ge", "As", "Se", "Br", "Kr", "Sb", "Te", "I", "Xe", "At", "Rn"],
    ["H", "Li", "Na", "K", "Rb", "Cs", "Fr"],
    ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"],
    ["N", "P", "As", "Sb", "Bi", "Mc"],
    ["O", "S", "Se", "Te", "Po", "Lv"],
    ["F", "Cl", "Br", "I", "At", "Ts"],
    ["He", "Ne","Ar", "Kr", "Xe", "Rn", "Og"],
    ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"],
    ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"],
    ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn"],
    ["Al", "Ga", "In", "Sn", "Tl", "Pb", "Bi", "Po"],
    ["B", "Si", "Ge", "As", "Sb", "Te", "At"],
    ["H", "C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I"],
    ["H", "He", "Li", "Be", "Na", "Mg", "K", "Ca", "Rb", "Sr", "Cs", "Ba", "Fr", "Ra"],
    ["B", "C", "N", "O", "F", "Ne", "Al", "Si", "P", "S", "Cl", "Ar", "Ga", "Ge", "As", "Se", "Br", "Kr", "In", "Sn", "Sb", "Te", "I", "Xe", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
    ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn"],
    ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"],
]

Diet_Description = [
    ["Oxygen, carbon, hydrogen, and nitrogen are the main building blocks of EVERY living creature, including human beings. Specifically, our body is primarily composed of just 11 elements, along with minimal traces of boron, chromium, cobalt, copper, fluorine, iodine, iron, manganese, molybdenum, selenium, silicon, nickel, bromine, vanadium, and zinc.\n\nIt seems incredible that a complex creature like the human is made up of only 26 types of building blocks: however, let's remember that these elements are not randomly piled up. Inside our body, atoms combine in thousands of ways to form simple compounds, which, in turn, are the building blocks of larger and more complex molecules. \n\n(Isaac Asimov 'The Building Blocks of the Universe', Milan: A. Mondadori, 1971)"],
    ["'Raw materials are crucial to Europe’s economy. They form a strong industrial base, producing a broad range of goods and applications used in everyday life and modern technologies. Reliable and unhindered access to certain raw materials is a growing concern within the EU and across the globe. To address this challenge, the European Commission has created a list of critical raw materials (CRMs) for the EU, which is subject to a regular review and update. CRMs combine raw materials of high importance to the EU economy and of high risk associated with their supply.' \n\n (https://single-market-economy.ec.europa.eu/sectors/raw-materials/areas-specific-interest/critical-raw-materials_en)"],
    ["'Mobile phones have a high embedded value of interest within a circular economy. With the number of these devices operating worldwide expected to reach 18bn by 2025 their low recycling rate leads to large tonnages of End-of-Life Mobile Phones (EoL-MPs) [...] due to increased demand for raw materials, increased energy, and water consumption, and, where uncontrolled and poor disposal at end-of-life occurs, significant impacts on health and the environment. EoL-MPs [...] include strategically and economically important high technology metals, many of which are classified as critical by the EU. [...] On average, the major mass fraction distributed in a mobile phone is: plastics (40%), metals (35%) and ceramics (25%). The results show that 1 tonne of EoL-MPs can contain up to 53 Kg copper, 141 g gold, 270 g silver, 10 g platinum, 18 g palladium and 3.3 Kg rare earth elements, among other valuable metals [...]. The calculated economic value of the EoL-MPs components is in the order: cameras (86,860 US$/ton), printed circuit boards (55,459 US$/ton), speakers (21,853 US$/ton) and screens (3,779 US$/ton). Based on the predicted 5 billion EoL-MPs discarded by the end of 2022, this waste stream has a potential economic value of US $ 9.25 billion. Use of EoL-MPs as a secondary resource-rich stream [...] offers a route to close the materials loop, helps to mitigate the threat to natural resources and the environmental and human health impacts arising from mining operations, relieves supply demands and contributes to the economy.' \n\nM. Gómez et al. Critical and strategic metals in mobile phones: A detailed characterisation of multigenerational waste mobile phones and the economic drivers for recovery of metal value, J Clean Prod 419 (2023)138099. https://doi.org/10.1016/j.jclepro.2023.138099"],
    ["'DNA is made up of carbon, hydrogen, oxygen, nitrogen and phosphorus' \n\nA. Rathi, Elements of life. Education in Chemistry 2011 https://edu.rsc.org/feature/elements-of-life/3007327.article"],
    ["'Radioactive elements are both naturally occurring and anthropogenic in origin, and can be found throughout the geosphere. Naturally occurring radioactive materials are dominated by members of the uranium and thorium decay chains, including radium and radon. Wastes containing elevated levels of these are frequently generated by human activities, such as mining and milling of uranium ore, coal burning, and water treatment. Anthropogenic radionuclides include transuranic elements (e.g., Pu, Np, Am) and fission products (e.g., 99Tc, 137Cs), which are produced by nuclear reactions. They are released to the environment during nuclear weapons production and testing and when power plant accidents occur. Spent nuclear fuel, currently stockpiled for eventual disposal, represents a huge reservoir of these materials. Once released to the environment, the behavior of these radionuclides is largely controlled by their geochemistry and by characteristics of the local environment. Aqueous concentrations are commonly determined by radionuclide solubility and sorption, which in turn are controlled by redox state, availability of mineral substrates for sorption, and concentrations of aqueous complexing agents. Here, the sources and environmental behavior of radionuclides, and the exposure pathways and health risks that they pose to human populations are summarized.'\n\nM.D. Siegel and C.R. Bryan, Radioactivity, Geochemistry, and Health. Treatise on Geochemistry (Second Edition) 2014, 191-256. https://doi.org/10.1016/B978-0-08-095975-7.00906-2"],
    ["'A true 'low-activation' material should ideally achieve all of the following objectives: \n1. The possible prompt dose at the site boundary from 100% release of the inventory should be <2 Sv (200 rem); hence, the design would be 'inherently safe' [...]\n2. The possible cancers from realistic releases should be limited such that the accident risk is <0.1%/yr of the existing background cancer risk to local residents [...]\n3. The decay heat should be limited so that active mitigative measures are not needed to protect the investment from cooling transients; hence, the design would be passively safe with respect to decay heat.\n4. Used materials could be either recycled or disposed of as near-surface waste.\n5. Hands-on maintenance should be possible around coolant system piping and components such as the heat exchanger.\n6. Effluents of activation products should be minor compared to the major challenge of limiting tritium effluents.\nGrades from A (best) to G (worst) are given to each element in the areas of accident safety, recycling, and waste management.\n[...]Designs focusing on these truly low-activation materials will help achieve the excellent safety and environmental potential of fusion energy.\n\n S. J. Piet et al. Initial Integration of Accident Safety, Waste Management, Recycling, Effluent, and Maintenance Considerations for Low-Activation Materials. Fusion Technology, 19(1991)46–161. doi:10.13182/fst19-1-146 "],
    ["Ge from Latin Germania, 'Germany'; the name was proposed by Dmitri Ivanovich Mendeleev (1834-1907), in honor of the discoverer, German chemist Clemens Winkler (1838-1904). Mendeleev had predicted its existence, naming it ekasilicon (eka- in Sanskrit means 'one'), because it was supposed to occupy an empty slot in his periodic table between silicon and tin.\nSm from Samarskij, in honor of the Russian geologist Vasilij Evgrafoviã Samarskij–Bychovec (1803–1870) who discovered a mineral, named in his honor 'samarskite', from which in 1880 Paul Emile Lecoq de Boisbaudran (1838-1912) isolated the new element.\nGd from Gadolin, in honor of the Finnish chemist and geologist Johan Gadolin (1760–1852), who discovered a mineral containing several elements belonging to the so-called rare earths, from which in 1880 the new element was isolated.\nBi from the Latin bisemutum, 'bismuth'; the etymology of this term, attributed to Paracelsus, the Latinized name of the Swiss physician Theophrastus Bombastus von Hohenheim (1493-1541), is debated. He traced it back to the German word Wissmut, because it was extracted (gemutet) in Saxony in the location of St. George in the meadows (in den Wiesen); according to others, it would instead derive from the ancient German Weissmuth, 'white material', because in its elemental state, bismuth is a shiny white metal; still, others claim its derivation from the Greek psimúthion, 'white pigment, white substance'. Currently, the most accredited origin seems to be the Arabic itmid, 'antimony', because in the past, bismuth was mistaken for antimony, which belongs to the same group as bismuth and has a very similar appearance.\nCm from the Latin curium, in honor of the spouses Marie Sklodowska Curie (1867-1934) and Pierre Curie (1859-1906), for their pioneering work in the field of radioactive elements.\nEs from Einstein; the element was first observed, along with fermium, at the end of 1952, examining the residues of the first test of a hydrogen bomb; for security reasons (during the Cold War), these results were kept secret until 1955: the name of the new element was then chosen to honor Albert Einstein (1879-1955), who had just passed away.\nFm from Fermi; the element was first observed, along with einsteinium, at the end of 1952, examining the residues of the first test of a hydrogen bomb; for security reasons (during the Cold War), these results were kept secret until 1955: the name of the new element was then chosen to honor the Italian physicist Enrico Fermi (1901-1954), who had passed away the previous year.\nMd from Mendeleev; synthesized in 1955, it was named in honor of the Russian chemist Dmitri Ivanovich Mendeleev (1834-1907).\nNo from Nobel; obtained in 1958 by a group comprising American and Scandinavian scientists, it was named in honor of the Swedish chemist Alfred Bernhard Nobel (1833-1896).\nLr from Lawrence; named in honor of the American scientist Ernest Orlando Lawrence (1901-1958), who built the first cyclotron; the symbol, initially Lw, was changed to the current one in 1961.\nRf from Rutherford, named in honor of the New Zealand physicist Ernest Rutherford (1871-1937); the new element was synthesized in 1964 in Dubna (Russia) and in 1969 in Berkeley (California); however, the Americans claimed that they had failed to reproduce the method used by the Soviets, leading to a dispute over the name, as the Russians proposed 'dubnium' (Db); the dispute was resolved in 1997 through a compromise involving the names of elements from 104 to 108.\nSg from Seaborg, the name of the American chemist Glenn Theodore Seaborg (1912-1999); the element was discovered almost simultaneously in 1974 in Dubna (Russia) and in Berkeley (California); the Americans proposed to dedicate it to Seaborg, who discovered about a dozen new elements, but who was still alive; this led to a dispute over the name, which was only resolved in 1997 through a compromise involving the names of elements from 104 to 108.\nBh from Bohr, in honor of the Danish physicist Niels Bohr (1885-1962); obtained in 1976 in Dubna (Russia), the discovery was confirmed five years later by a German group, which proposed the name nielsbohrium to avoid confusion with boron; however, in 1997, the current name was established.\nMt from Meitner, in honor of the Austrian-Swedish physicist and mathematician Lise Meitner (1878-1968), who first understood the mechanism of nuclear fission.\nRg from Roentgen, in honor of the German physicist Wilhelm Conrad Roentgen (1845-1923), who discovered X-rays on December 8, 1895, exactly 99 years before the element was first synthesized (in reality, only three atoms were obtained).\nOg discovered in 1996; recently, the name 'copernicium' has been proposed in honor of the Polish astronomer Mikołaj Kopernik (1473-1543), better known by his Latinized name Nicolaus Copernicus, who contributed to the affirmation of the heliocentric theory; recognition of the name with the symbol Cn is imminent (although the original proposal was Cp).\n\nF. Tottola M. Righetti A. Allegrezza Chimica per noi A. Mondadori Scuola © by Mondadori Education, 2010"],
    ["B from the French bore, which is from the Latin borax, 'borax', a compound in which boron is abundant; 'borax' in turn derives from the Persian burak, 'saltpeter', similar in appearance to borax and with which it could be confused.\nC from the Latin carbo, 'coal', composed predominantly of carbon; it is one of the nine elements known since antiquity, along with gold, silver, copper, sulfur, tin, lead, mercury, and iron.\nF from the Latin fluere, 'to flow'; its minerals indeed (for example, fluorite) facilitate the fusion of minerals.\nNa from Latin salsola soda, name of the plant from whose ashes a compound, 'soda', is obtained; the symbol, however, comes from natrium, the Latin name for soda, derived from the Arabic natrun, indicating a lake (today's Natron, in Tanzania) where it abounds.\nAl from the Latin alumen, 'alum', in which it is contained.\nSi from Latin silex, 'flint', a silicon mineral.\nS from Latin sulphur, 'sulfur', of pre-Latin origin; it is indeed one of the nine elements known since antiquity, along with carbon, gold, silver, copper, tin, lead, mercury, and iron.\nK from English pot, 'pot, vessel', and ash, 'ash'; named so by Humphry Davy (1778-1829), who isolated it in 1807 by treating the residue of the calcination of certain plants. The symbol K derives from the Latin name kalium, itself from the Arabic al qali.\nCa from Latin calx, 'lime', of which it is a compound.\nSc from Latin Scandia, 'Scandinavia'; because it was first isolated (1879) from a Swedish mineral; its existence had been predicted by Dmitri Ivanovich Mendeleev (1834-1907), who had named it ekaboron (eka- in Sanskrit means 'one'), because it was supposed to occupy an empty slot in his periodic table next to boron.\nMn from Latin Magnésion, 'Magnesia', a city in Thessaly near which there were deposits of magnetic ore strongly resembling pyrolusite, a black manganese compound. According to others, the name may derive directly from the corruption of the Latin magalaea, an ancient name for pyrolusite.\nFe from Latin ferrum, 'iron'; is one of the nine elements known since antiquity, along with carbon, gold, silver, copper, sulfur, tin, lead, and mercury.\nCu from Late Latin aeramen, copper, bronze (the Latins did not distinguish between copper and its alloy); in 77 A.D., Pliny replaced it with cuprum, copper, Cyprian bronze, an island where it is found in abundance; from this name derives the symbol Cu; is one of the nine elements known since antiquity, along with carbon, gold, silver, sulfur, tin, lead, mercury, and iron.\nGa from Latin Gallium, Latinized surname of the discoverer, French chemist Paul Emile Lecoq de Boisbaudran (1838-1912). In French, coq means 'the rooster', in Latin gallus; moreover, Gaul, in Latin, is the name of modern-day France.\nGe from Latin Germania, 'Germany'; the name was proposed by Dmitri Ivanovich Mendeleev (1834-1907), in honor of the discoverer, German chemist Clemens Winkler (1838-1904). Mendeleev had predicted its existence, naming it ekasilicon (eka- in Sanskrit means 'one'), because it was supposed to occupy an empty slot in his periodic table between silicon and tin.\nRb from Latin rubidum, 'dark red'; for the characteristic color of the lines of its emission spectrum.\nRu from Latin Ruthenia, 'Russia'; proposed by Karl K. Klaus (1796-1864), who discovered it in 1844, in honor of his own country.\nPd from Latin Pallas, 'Pallas'; of the asteroid discovered in 1802, just one year before the element.\nIn from Latin indium, 'indigo'; for the color of its spectral lines that allowed it to be identified.\nSn from Latin stannum, 'tin'; the term was used by Pliny the Elder in reference to an alloy of silver and lead, rather than to tin itself, known at the time as white lead; tin is one of the nine elements known since antiquity, along with carbon, gold, silver, copper, sulfur, lead, mercury, and iron.\nSb from Arabic al ithmid, 'antimony'; according to others, 'antimony' would derive from Greek antí-, 'against' and mónos, 'alone': against solitude (in a broad sense), as it is always associated with other minerals. The symbol instead derives from Latin stibium, 'antimony' (actually a cosmetic based on antimony used to blacken eyebrows).\nTe from Latin tellus, 'Earth'; discovered in 1782 by Franz-Joseph Müller von Reichenstein (1742-1825), it was named with the current name in 1798 by Martin Heinrich Klaproth (1743-1817), who first succeeded in isolating it, perhaps in opposition to the name 'uranium' assigned to the element he himself discovered in 1789.\nCs from Latin caesius, 'bluish-gray'; for the color of its spectral lines.\nLa from Greek lantháno, 'to lie hidden'; so named for its difficulty in isolation.\nCe from Latin Ceres, 'Ceres', the Roman goddess of agriculture and fertility, a name that had been given to an asteroid discovered in 1801, two years before the element.\nPm from Latin Prometheus, 'Prometheus', the Titan who stole fire from Zeus and gave it to mankind. The only artificial element of the Lanthanides, its name, proposed by the wife of Charles D. Coryell (1912–1971), one of the discoverers, recalls that it can be obtained in significant quantities using the 'fire' produced by nuclear fission reactions.\nEu from Latin Europa, because it was discovered in Europe.\nHo from Latin Holmia, meaning 'Stockholm'; near the Swedish city, many minerals (gadolinite, euxenite, and others) rich in a rare earth, originally thought to be an element (yttrium), were found, from which this element was later separated.\nTm from Latin thulium, from Thule, 'Tule', a location on the North Sea considered in ancient times to be the northernmost limit of the known world and an archaic name for Scandinavia.\nLu from Latin Lutetia, 'Paris'; the name was chosen by Georges Urbain (1872-1938), who discovered it in 1907, in honor of his own city; in the same year, independently, it was also isolated by the Austrian Carl Auer Freiherr von Welsbach (1858–1929), who proposed the name 'cassiopium' (still used by some German scientists) to remember the famous constellation Cassiopeia, easily recognizable because its five stars form an almost perfect W, the initial of Welsbach's surname.\nHf from Latin Hafnia, 'Copenhagen', because it was discovered in this city in 1923 by Dirk Coster (1889-1950) and George Charles de Hevesy (1885-1966). A decade before its official discovery, based on some weak experimental evidence of its existence, some French researchers had assigned the name 'celtium' to the missing element with atomic number 72, from Latin Celtae, 'Celts', ancient inhabitants of France: but this name was not retained.\nTa from Latin Tantalus, 'Tantalus', the mythical king of Lydia condemned by the gods to a gruesome punishment: among other things, despite being surrounded by water, he could not drink it; the name would therefore allude to the fact that the element is unaffected by common acids.\nIr from Latin Íris, 'Iris', messenger of the gods and goddess of the rainbow; for the intense coloration of many of its salts.\nAu from the Latin aurum, 'gold', of Indo-European origin; it is one of the nine elements known since antiquity, along with carbon, silver, copper, sulfur, tin, lead, mercury, and iron. \nHg from the Latin Mercurius, 'Mercury', ancient Roman deity, son of Jupiter and the first planet of the solar system, associated with the element according to alchemists. The symbol is from the Greek hýdor, 'water', and árgyros, 'silver': 'liquid silver', because, at ambient temperature and pressure, it is liquid and similar in color to silver; it is one of the nine elements known since antiquity, along with carbon, gold, silver, copper, sulfur, tin, lead, and iron. \nBi from the Latin bisemutum, 'bismuth'; the etymology of this term, attributed to Paracelsus, the Latinized name of the Swiss physician Theophrastus Bombastus von Hohenheim (1493-1541), is debated. He traced it back to the German word Wissmut, because it was extracted (gemutet) in Saxony in the location of St. George in the meadows (in den Wiesen); according to others, it would instead derive from the ancient German Weissmuth, 'white material', because in its elemental state, bismuth is a shiny white metal; still, others claim its derivation from the Greek psimúthion, 'white pigment, white substance'. Currently, the most accredited origin seems to be the Arabic itmid, 'antimony', because in the past, bismuth was mistaken for antimony, which belongs to the same group as bismuth and has a very similar appearance.\nBi from the Latin bisemutum, 'bismuth'; the etymology of this term, attributed to Paracelsus, the Latinized name of the Swiss physician Theophrastus Bombastus von Hohenheim (1493-1541), is debated. He traced it back to the German word Wissmut, because it was extracted (gemutet) in Saxony in the location of St. George in the meadows (in den Wiesen); according to others, it would instead derive from the ancient German Weissmuth, 'white material', because in its elemental state, bismuth is a shiny white metal; still, others claim its derivation from the Greek psimúthion, 'white pigment, white substance'. Currently, the most accredited origin seems to be the Arabic itmid, 'antimony', because in the past, bismuth was mistaken for antimony, which belongs to the same group as bismuth and has a very similar appearance.\nPo from the Latin Polonia, 'Poland', native country of Marie Sklodowska Curie (1867-1934), who discovered it in 1898.\nRn from the Latin radius, 'ray'; discovered in 1898 by Marie Sklodowska Curie (1867-1934), the name, proposed by the German chemist Curt Schmidt in 1918, was chosen to recall its radioactivity and because it shared the etymological origin with radium, from which it is obtained as a decay product.\nRa from the Latin radius, 'ray'; originally, the name referred to its most important isotope, 226, first discovered; it was later extended to the element to evoke its property of emitting rays capable of impressing a photographic plate, then called 'radioactivity'. Discovered in 1898 by Marie Sklodowska Curie (1867-1934), it is the most famous among the naturally occurring radioactive elements (and the heaviest of the alkaline earth metals group).\nNp from the Latin Neptunus, 'Neptune'; the Roman god of the sea, it gives its name to the planet of the solar system that immediately follows Uranus: hence it was assigned to the element that follows it in the periodic table.\nCm from the Latin curium, in honor of the spouses Marie Sklodowska Curie (1867-1934) and Pierre Curie (1859-1906), for their pioneering work in the field of radioactive elements.\nHs from the Latin Hassia, the Latinized name of Hesse, the German region where Darmstadt is located and where it was first produced (1984).\n\nF. Tottola M. Righetti A. Allegrezza Chimica per noi A. Mondadori Scuola © by Mondadori Education, 2010"],
    ["H from Greek hýdor, 'water', and ghennáo, 'to generate': 'water generator'; it was proposed by Antoine Laurent Lavoisier (1743-1794) following the model of 'oxygen'\nHe from the Greek hélios, meaning 'Sun'; before being isolated by William Ramsay (1852–1916) in 1895, the element had been detected in the spectrum of solar light during the total solar eclipse of 1868 and is the only element discovered in an extraterrestrial object before being found on Earth.\nLi from the Greek lítheios, meaning 'of stone'; its related minerals indeed have a stony appearance. \nBe from the Greek béryllos, 'beryl', the name, of Indian origin, of a precious stone of bluish-green color: aquamarine (bluish-green) and emerald (green) are beryl minerals with specific impurities.\nN from the Greek a- (privative alpha) and zotikós, 'life-giving': 'non-life producer'; the name was coined by Antoine Laurent Lavoisier (1743-1794); the symbol is instead derived from 'nitrogen', from the Greek nítron, 'saltpeter', and ghennáo, 'to generate': 'saltpeter generator', a name proposed by Jean-Antoine Chaptal (1756-1832) used in the English language but no longer in use in Italy.\nO from the Greek oxýs, 'acid', and ghennáo, 'to generate': 'acid generator'; name proposed by Antoine Laurent Lavoisier (1743-1794) mistakenly convinced that oxygen was part of the composition of all acids.\nNe from Greek néos, 'new'; so named by William Ramsay's son (1852-1916), who discovered it along with Morris Travers (1872-1961) in 1898, because it was 'another new gas' present in the air.\nP from Greek phôs, 'light', and -phoro, 'carrier': 'light-bringer', with reference to its extreme reactivity, by virtue of which, when combined with oxygen, it emits a faint luminescence.\nCl from Greek khlorós, 'green', for its color.\nAr from Greek from a- (negative alpha privative) and érgon, 'work': 'inactive', so named because it does not react with other elements.\nTi from Greek titán, 'Titan', a generic name for the six mythological giants sons of Uranus (Heaven) and Gaia (Earth); so named for its high mechanical resistance.\nCr from Greek khrôma, 'color'; named for the colors of its compounds.\nCo from Greek kóbalos, 'goblin': because it was believed that a goblin had substituted cobalt for the desired silver for the miners.\nAs from Greek arsenikón, 'male, masculine', in the sense of 'bold', for its action on metals.\nSe from Greek seléne, 'Moon', for its brightness; since the element is similar to tellurium, with which it was initially confused, Jöns Jacob Berzelius (1779-1848) argued that its name should also reflect this similarity, and therefore the Greek word for Moon, the Earth's only satellite, was chosen.\nBr from Greek brômos, 'bad smell'; so named because, at ambient temperature and pressure, it is a reddish-brown liquid with an unpleasant and suffocating odor.\nKr from Greek kryptón, 'hidden'; named by William Ramsay (1852-1916), who discovered it along with Morris Travers (1872-1961) in 1898, because of its difficult detection (it is found in very small quantities in the gases that form atmospheric air).\nNb from Greek Niobe, 'Niobe', mythical daughter of the King of Lydia Tantalus; because it is similar to tantalum. Charles Hatchett (1765-1847), its discoverer, had named it columbium (Cb); the name 'niobium', proposed by H. Rose (1759-1864), was definitively adopted only in 1949.\nMo from Greek mólybdos, 'lead'; was named by J. J. Berzelius (1779-1848) for its resemblance to lead.\nTc from Greek tekhnetós, 'artificial'; does not exist in nature: it is the first element to be produced artificially and the only artificial one among the transition elements; it was obtained in 1937 by the Italians Carlo Perrier (1886-1948) and Emilio Segrè (1905-1989). Previously (1925), the discovery of element 43 had been announced by Walter Noddack (1893-1960), who had named it 'masurium' (from Masuria, the region of origin of his family, now in Poland), but the discovery had not been confirmed.\nRh from Greek rhódon, 'rose'; from the color of the aqueous solutions of its salts.\nAg from Greek árgyros, 'silver', in turn from argós, 'white, shining'; is one of the nine elements known since antiquity, along with carbon, gold, copper, sulfur, tin, lead, mercury, and iron.\nCd from Greek kadmeía (gê), '(earth) of Cadmus', namely Thebes, the Greek city founded by the mythical hero Cadmus; cadmium was indeed discovered in various zinc mines and especially in the mineral calamine, extracted near the fortress of Thebes.\nSb from Arabic al ithmid, 'antimony'; according to others, 'antimony' would derive from Greek antí-, 'against' and mónos, 'alone': against solitude (in a broad sense), as it is always associated with other minerals. The symbol instead derives from Latin stibium, 'antimony' (actually a cosmetic based on antimony used to blacken eyebrows).\nI from Greek iódes, 'violet'; for the color of its vapors.\nXe from Greek ksénos, 'stranger, guest'; so named by discoverers William Ramsay (1852-1916) and Morris Travers (1872-1961), as it was found in the fractionation of the rare gases krypton and neon.\nBa from Greek barýs, 'heavy'; the name is derived from that of barite, the most important mineral from which it is extracted, formerly known as 'heavy earth' referring to its high density, about twice that of other compounds with a similar appearance.\nLa from Greek lantháno, 'to lie hidden'; so named for its difficulty in isolation.\nPr from Greek prasêos, a misreading of prásinos, 'green, leek color', and dídymos, 'twin'. In 1839, the Swedish chemist Carl Gustaf Mosander (1797–1858) believed he had discovered a new element which he called 'didymium', suspecting it to be actually a mixture. In 1885, Carl Auer Freiherr von Welsbach (1858–1929) identified two elements in didymium, named neodymium and praseodymium, the latter for the color of some of its compounds.\nNd from Greek néos, 'new', and dídymos, 'twin'; is the second element isolated from 'didymium', alongside praseodymium.\nDy from Greek dysprósitos, 'hard to reach'; owes its name to the enormous difficulty encountered by Paul Emile Lecoq de Boisbaudran (1838-1912), who discovered it in 1886, in separating it from other elements belonging to the so-called rare earths.\nOs from Greek osmé, 'smell'; for the strong odor of the tetroxide, volatile.\nTl from the Greek thallós, 'green shoot'; because, as Sir William Crookes (1832–1919) stated when he discovered it in 1861 through spectroscopic investigations, the characteristic green line present in its spectrum 'vividly recalls the fresh color of vegetation in this season'.\nBi from the Latin bisemutum, 'bismuth'; the etymology of this term, attributed to Paracelsus, the Latinized name of the Swiss physician Theophrastus Bombastus von Hohenheim (1493-1541), is debated. He traced it back to the German word Wissmut, because it was extracted (gemutet) in Saxony in the location of St. George in the meadows (in den Wiesen); according to others, it would instead derive from the ancient German Weissmuth, 'white material', because in its elemental state, bismuth is a shiny white metal; still, others claim its derivation from the Greek psimúthion, 'white pigment, white substance'. Currently, the most accredited origin seems to be the Arabic itmid, 'antimony', because in the past, bismuth was mistaken for antimony, which belongs to the same group as bismuth and has a very similar appearance.\nAt from the Greek a- (negative prefix) and statós, 'stable'; the only element among the so-called halogens to decay radioactively, it was discovered in 1940 by the Italian physicist Emilio Segrè (1905-1989).\nAc from the Greek aktís, 'ray'; the name was proposed in 1881 with reference to the luminescent effect produced by light on its salts.\nPa from the Greek prôtos, 'first', and aktínion, 'actinium'; initially, protactinium was called 'brevium', from Latin brevium, for its short half-life, while protactinium designated the isotope 231 which, with a half-life of 32,480 years, 'precedes' the isotope 227 of actinium in the radioactive decay of uranium.\nU from the Greek Ouranós, 'Uranus'; identified in 1789 by Martin Heinrich Klaproth (1743-1817), it was named after the planet Uranus, discovered eight years earlier.\nPu from the Greek Plúton, 'Pluto', the Greek god of the underworld and celestial body, initially considered the ninth planet of the solar system, after Neptune: for this reason, the name of the element that follows neptunium in the periodic table was derived from it, also discovered in 1940, a few months earlier.\n\nF. Tottola M. Righetti A. Allegrezza Chimica per noi A. Mondadori Scuola © by Mondadori Education, 2010"],
    ["Mg from Magnesia, a city in Thessaly, from which the stone of the same name used as a purgative originated; according to the ancients, it had to be brought near a magnet, which is named after the Greek city of Magnesia: just as the magnet attracted iron, so magnesium had the property of attracting bodily humors.\nSc from Latin Scandia, 'Scandinavia'; because it was first isolated (1879) from a Swedish mineral; its existence had been predicted by Dmitri Ivanovich Mendeleev (1834-1907), who had named it ekaboron (eka- in Sanskrit means 'one'), because it was supposed to occupy an empty slot in his periodic table next to boron.\nMn from Latin Magnésion, 'Magnesia', a city in Thessaly near which there were deposits of magnetic ore strongly resembling pyrolusite, a black manganese compound. According to others, the name may derive directly from the corruption of the Latin magalaea, an ancient name for pyrolusite.\nGa from Latin Gallium, Latinized surname of the discoverer, French chemist Paul Emile Lecoq de Boisbaudran (1838-1912). In French, coq means 'the rooster', in Latin gallus; moreover, Gaul, in Latin, is the name of modern-day France.\nGe from Latin Germania, 'Germany'; the name was proposed by Dmitri Ivanovich Mendeleev (1834-1907), in honor of the discoverer, German chemist Clemens Winkler (1838-1904). Mendeleev had predicted its existence, naming it ekasilicon (eka- in Sanskrit means 'one'), because it was supposed to occupy an empty slot in his periodic table between silicon and tin.\nSe from Greek seléne, 'Moon', for its brightness; since the element is similar to tellurium, with which it was initially confused, Jöns Jacob Berzelius (1779-1848) argued that its name should also reflect this similarity, and therefore the Greek word for Moon, the Earth's only satellite, was chosen.\nSr from Strontian, the name of the Scottish village (Western Highlands) where strontianite was extracted from mines, the mineral from which it was isolated.\nY from Ytterby, the name of the Swedish city from which a mineral, 'ytterbite', rich in new rare earth elements (such as erbium, terbium, and ytterbium), was extracted; initially, the name 'yttrium' was indeed attributed to a substance that later turned out to be a mixture of new elements (including yttrium, ytterbium, and holmium): that's why yttrium has a chemical symbol of a single letter and ytterbium of two.\nNb from Greek Niobe, 'Niobe', mythical daughter of the King of Lydia Tantalus; because it is similar to tantalum. Charles Hatchett (1765-1847), its discoverer, had named it columbium (Cb); the name 'niobium', proposed by H. Rose (1759-1864), was definitively adopted only in 1949.\nTc from Greek tekhnetós, 'artificial'; does not exist in nature: it is the first element to be produced artificially and the only artificial one among the transition elements; it was obtained in 1937 by the Italians Carlo Perrier (1886-1948) and Emilio Segrè (1905-1989). Previously (1925), the discovery of element 43 had been announced by Walter Noddack (1893-1960), who had named it 'masurium' (from Masuria, the region of origin of his family, now in Poland), but the discovery had not been confirmed.\nRu from Latin Ruthenia, 'Russia'; proposed by Karl K. Klaus (1796-1864), who discovered it in 1844, in honor of his own country.\nPd from Latin Pallas, 'Pallas'; of the asteroid discovered in 1802, just one year before the element.\nCd from Greek kadmeía (gê), '(earth) of Cadmus', namely Thebes, the Greek city founded by the mythical hero Cadmus; cadmium was indeed discovered in various zinc mines and especially in the mineral calamine, extracted near the fortress of Thebes.\nTe from Latin tellus, 'Earth'; discovered in 1782 by Franz-Joseph Müller von Reichenstein (1742-1825), it was named with the current name in 1798 by Martin Heinrich Klaproth (1743-1817), who first succeeded in isolating it, perhaps in opposition to the name 'uranium' assigned to the element he himself discovered in 1789.\nEu from Latin Europa, because it was discovered in Europe.\nTb from Ytterby, the name of the Swedish city from which a mineral, ytterbite, rich in new elements belonging to the rare earths (such as yttrium, ytterbium, and erbium), was extracted.\nHo from Latin Holmia, meaning 'Stockholm'; near the Swedish city, many minerals (gadolinite, euxenite, and others) rich in a rare earth, originally thought to be an element (yttrium), were found, from which this element was later separated.\nEr from Ytterby, the name of the Swedish city where a mineral called ytterbite, rich in new elements belonging to the rare earths (such as yttrium, erbium, and erbium), was extracted.\nTm from Latin thulium, from Thule, 'Tule', a location on the North Sea considered in ancient times to be the northernmost limit of the known world and an archaic name for Scandinavia.\nYb from Ytterby, the name of the Swedish city where a mineral called ytterbite, rich in new elements belonging to the rare earths (such as yttrium, ytterbium, and erbium), was extracted.\nLu from Latin Lutetia, 'Paris'; the name was chosen by Georges Urbain (1872-1938), who discovered it in 1907, in honor of his own city; in the same year, independently, it was also isolated by the Austrian Carl Auer Freiherr von Welsbach (1858–1929), who proposed the name 'cassiopium' (still used by some German scientists) to remember the famous constellation Cassiopeia, easily recognizable because its five stars form an almost perfect W, the initial of Welsbach's surname.\nHf from Latin Hafnia, 'Copenhagen', because it was discovered in this city in 1923 by Dirk Coster (1889-1950) and George Charles de Hevesy (1885-1966). A decade before its official discovery, based on some weak experimental evidence of its existence, some French researchers had assigned the name 'celtium' to the missing element with atomic number 72, from Latin Celtae, 'Celts', ancient inhabitants of France: but this name was not retained.\nRe from German Rheinland, 'Rhineland', the region of birth of the daughter of Walter Noddack (1893-1960) and Ida (1896-1978) who, together with Otto Berg (1873-1939), discovered it in 1925.\nBi from the Latin bisemutum, 'bismuth'; the etymology of this term, attributed to Paracelsus, the Latinized name of the Swiss physician Theophrastus Bombastus von Hohenheim (1493-1541), is debated. He traced it back to the German word Wissmut, because it was extracted (gemutet) in Saxony in the location of St. George in the meadows (in den Wiesen); according to others, it would instead derive from the ancient German Weissmuth, 'white material', because in its elemental state, bismuth is a shiny white metal; still, others claim its derivation from the Greek psimúthion, 'white pigment, white substance'. Currently, the most accredited origin seems to be the Arabic itmid, 'antimony', because in the past, bismuth was mistaken for antimony, which belongs to the same group as bismuth and has a very similar appearance.\nPo from the Latin Polonia, 'Poland', native country of Marie Sklodowska Curie (1867-1934), who discovered it in 1898.\nFr from French France, 'France', homeland of Marguerite Catherine Perey (1909-1975), the scientist who discovered it in 1939.\nU from the Greek Ouranós, 'Uranus'; identified in 1789 by Martin Heinrich Klaproth (1743-1817), it was named after the planet Uranus, discovered eight years earlier.\nNp from the Latin Neptunus, 'Neptune'; the Roman god of the sea, it gives its name to the planet of the solar system that immediately follows Uranus: hence it was assigned to the element that follows it in the periodic table.\nPu from the Greek Plúton, 'Pluto', the Greek god of the underworld and celestial body, initially considered the ninth planet of the solar system, after Neptune: for this reason, the name of the element that follows neptunium in the periodic table was derived from it, also discovered in 1940, a few months earlier.\nAm  from English America, in honor of the continent where it was obtained, in 1944, and for symmetry, because it is found below europium in the periodic table.\nBk from Berkeley, the name of the Californian city where it was obtained in 1949.\nCf from California, the name of the state in which it was first synthesized in 1949.\nDb from Dubna, the Russian town where it was first produced in 1970; subsequently, American scientists who had unsuccessfully attempted to confirm the discovery using other methods proposed the name 'hahnium', in honor of Otto Hahn (1879-1968), leading to a dispute over the name, which was only resolved in 1997 through a compromise involving the names of elements from 104 to 108.\nHs from the Latin Hassia, the Latinized name of Hesse, the German region where Darmstadt is located and where it was first produced (1984).\nDs from Darmstadt, the city where the Nuclear Research Center is located and where the element was synthesized in 1994; it seems that the name 'policium' was also proposed, as 110 is also the emergency number of the German police.\n\nF. Tottola M. Righetti A. Allegrezza Chimica per noi A. Mondadori Scuola © by Mondadori Education, 2010."],
    ["V from Vanadis, goddess of beauty in Norse mythology: for the beauty and variety of colors of its compounds.\nNi from German Kupfernickel, 'copper goblin': what miners claimed prevented them from finding copper.\nZn from German Zink, 'zinc', term of uncertain etymology.\nZr from Arabic zerqun, 'golden color', in turn from Persian azargun, composed of azar, 'fire', and gun, 'color'.\nSb from Arabic al ithmid, 'antimony'; according to others, 'antimony' would derive from Greek antí-, 'against' and mónos, 'alone': against solitude (in a broad sense), as it is always associated with other minerals. The symbol instead derives from Latin stibium, 'antimony' (actually a cosmetic based on antimony used to blacken eyebrows).\nW from Swedish tung, 'heavy', and sten, 'stone': 'heavy stone', alluding to its high specific weight; the symbol is instead derived from 'wolfram', another name by which it is known, derived from 'wolframite', the mineral from which it is extracted; of uncertain etymology, this name seems to be linked to the German Wolf, 'wolf', with which the alchemists indicated substances capable of 'stealing' tin from the fusion bath.\nPt from Spanish platina, from plata, 'silver'; for its color very similar to that of silver.\nTh from Swedish Thor, the god of thunder in Norse mythology; the name was proposed by Jöns Jacob Berzelius (1779-1848), who discovered it in 1828.\n\nF. Tottola M. Righetti A. Allegrezza Chimica per noi A. Mondadori Scuola © by Mondadori Education, 2010"],
    ["Take a look on Ptable: https://ptable.com/?lang=it#Propriet%C3%A0"],
    ["Take a look on Ptable: https://ptable.com/?lang=it#Propriet%C3%A0"],
    ["Take a look on Ptable: https://ptable.com/?lang=it#Propriet%C3%A0"],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# Constants for the game
SPEED = 100
SIZE = 20
PIECES = 3
SNAKE_COLOR = "#96AE21"
RAT_COLOR = "#E51A4B"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = "#002F5F"

# Define the main menu options
main_menu_options = ["New Game", "Exit"]

# Create the main window
window = Tk()
window.title("Jörmungandr's Elemental Diets: The World Snake")
window.resizable(False, False)


# Function to ask for diet selection before starting a new game
def ask_for_diet_selection():
    diet_selection_window = Toplevel(window)
    diet_selection_window.title("Select Diet")
    diet_selection_window.geometry("300x100")

    selected_diet_var = StringVar(diet_selection_window)
    selected_diet_var.set(Diets_list[0])  # Set default value to the first diet in the list

    diet_dropdown = OptionMenu(diet_selection_window, selected_diet_var, *Diets_list)
    diet_dropdown.pack(pady=10)

    start_game_button = Button(diet_selection_window, text="Start Game", command=lambda: start_new_game(selected_diet_var.get(), diet_selection_window))
    start_game_button.pack()

def show_diet_description(selected_diet):
    index = Diets_list.index(selected_diet)
    description = Diet_Description[index]
    return description

# Function to start a new game
def start_new_game(selected_diet, window_to_close):
    window_to_close.destroy()  # Close the diet selection window
    window.after(5, clear_game_over_elements)
    canvas.delete("game_over_label") 
    global score, direction, diet
    score = 0
    direction = 'down'
    diet = selected_diet
    label.config(text="Jörmungandr is hungry of \n{}\     Eaten: {}          |        It cannot eat Thor!".format(diet, score))
    canvas.delete("all")
    snake = Snake()
    food = Food()
    next_turn(snake, food)

# Function to handle menu selection
def menu_action(selection):
    if selection == "New Game":
        ask_for_diet_selection()  # Ask for diet selection before starting the game
    elif selection == "Exit":
        window.destroy()

# Create a dropdown menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
for option in main_menu_options:
    file_menu.add_command(label=option, command=lambda opt=option: menu_action(opt))



# Function to start a new game

# Create the score label
score = 0
direction = 'down'
diet = Diets_list [0]
label = Label(window, text="Jörmungandr is hungry of \n{}\n     Eaten: {}          |        It cannot eat Thor!   ".format(diet, score), font=('Corbel', SIZE))
label.pack()

# Create the canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()

# Create a dropdown menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
for option in main_menu_options:
    file_menu.add_command(label=option, command=lambda opt=option: menu_action(opt))


# Define the Snake class
class Snake:

    def __init__(self):
        self.body_size = PIECES
        self.coordinates = []
        self.squares = []

        for i in range(0, PIECES):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Define the Food class
class Food:

    # Define selectRandom function outside the class
    def selectRandom(self, elements):
        return random.choice(elements)

    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH / SIZE) - 1) * SIZE
        y = random.randint(0, (WINDOW_HEIGHT / SIZE) - 1) * SIZE

        self.coordinates = [x, y]

        elm = self.selectRandom(elements)  # Call selectRandom using self
        self.element_text = canvas.create_text(x + SIZE/2, y + SIZE/2, text=elm, fill=RAT_COLOR, font=('Corbel 18 bold'), tag="food")

def next_turn(snake, food):
    global space_pressed, score, diet

    if space_pressed:
        element_changed = canvas.itemcget(food.element_text, "text")

        #Balancing the scores so that continuously pressing the space bar does not give any advantage
        if element_changed in Elements_of_Diet[Diets_list.index(diet)]:
            score -= round(len(elements)/len(Elements_of_Diet[Diets_list.index(diet)]))
        else:
            score += round(len(elements)/(len(elements) - len(Elements_of_Diet[Diets_list.index(diet)])))


        label.config(text="Jörmungandr is hungry of \n{}\n     Eaten: {}         |        It cannot eat Thor!   ".format(diet, score))
        canvas.delete("food")
        food = Food()
        space_pressed = False  # Resetta la variabile space_pressed

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SIZE
    elif direction == "down":
        y += SIZE
    elif direction == "left":
        x -= SIZE
    elif direction == "right":
        x += SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        element_eaten = canvas.itemcget(food.element_text, "text")
        if element_eaten in Elements_of_Diet[Diets_list.index(diet)]:
            score += round(len(elements)/(len(elements) - len(Elements_of_Diet[Diets_list.index(diet)])))
        else:
            score -= round(len(elements)/len(Elements_of_Diet[Diets_list.index(diet)]))
        label.config(text="Jörmungandr is hungry of \n{}\n     Eaten: {}            |     It cannot eat Thor!   ".format(diet, score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over(diet)
    else:
        window.after(SPEED, next_turn, snake, food)



# Function to handle direction change
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Function to check for collisions
def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WINDOW_WIDTH:
        return True
    elif y < 0 or y >= WINDOW_HEIGHT:
        return True
    elif canvas.itemcget(food.element_text, "text") == "Th":
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Function to change food
def replace_food(event):
    global space_pressed
    space_pressed = True
window.bind('<space>', replace_food)

# Function to handle game over
def game_over(selected_diet):
    global game_over_label, diet_description_label

    canvas.delete(ALL)
    game_over_label = Label(canvas, text="[Stay Hungry] [Stay Periodic]", font=('Corbel', 30), fg=RAT_COLOR, bg=BACKGROUND_COLOR)
    game_over_label.pack(pady=20)
    diet_description = show_diet_description(selected_diet)
    diet_description_label = Text(canvas, wrap="word", font=('Corbel', 11), bg=BACKGROUND_COLOR, fg="white")
    diet_description_label.insert(END, diet_description)
    diet_description_label.pack(expand=True, fill=BOTH)
    

# Function to clear game over elements
def clear_game_over_elements():
    global game_over_label, diet_description_label

    if game_over_label:
        game_over_label.destroy()
        game_over_label = None
    if diet_description_label:
        diet_description_label.destroy()
        diet_description_label = None



window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind keys for controlling the snake throughh arrow and leter. This provides flexibility in controlling the game, allowing players to choose their preferred control method.
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<KeyPress-a>', lambda event: change_direction('left'))
window.bind('<KeyPress-A>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<KeyPress-d>', lambda event: change_direction('right'))
window.bind('<KeyPress-D>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<KeyPress-w>', lambda event: change_direction('up'))
window.bind('<KeyPress-W>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<KeyPress-s>', lambda event: change_direction('down'))
window.bind('<KeyPress-S>', lambda event: change_direction('down'))




snake = Snake()
food = Food()
space_pressed = False
next_turn(snake, food)
game_over_label = None
diet_description_label = None

# Run the main event loop
window.mainloop()

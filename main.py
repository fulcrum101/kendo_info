import streamlit as st
from streamlit.components.v1 import html


def main():
    st.set_page_config(
        page_title='#kendo_in_latvia',
        page_icon='⛩️'
    )
    st.image('images/header.jpg')
    st.title('Latvijas Kendo federācija')
    st.caption('pārstāv [Starptautisko Kendo federāciju (FIK)](http://www.kendo-fik.org), [Eiropas Kendo federāciju](https://www.ekf-eu.com) un [Visjapānas Kendo federāciju Latvijas teritorijā](https://www.kendo.or.jp/en/), kā arī  ir [Latvijas Sporta federāciju padomes](https://lsfp.lv) atzīta sporta federācija.')
    st.divider()

    col1, col2 = st.columns(2)

    col1.header('Saites')
    col1.markdown('''
    - **kendo.lv** mājas lapa [➤](kendo.lv)
    - **@LatvijasKendoFederacija** Facebook [➤](https://www.facebook.com/LatvijasKendoFederacija/)
    - **@kendo_in_latvia** Instagram [➤](https://www.instagram.com/kendo_in_latvia/)
    - **@KendoInLatvia** YouTube [➤](https://www.youtube.com/@KendoInLatvia)''')

    col2.header('Kontakti')
    col2.markdown('''
    - 👤 **Kontaktpersona:** Vladimirs Kindzulis
    - 📞 **Tel. nr:** [+371 29217637](callto:0037129217637)
    - ✉️ **E-pasts:** [kwon@apollo.lv](mailto:kwon@apollo.lv)''')

    st.info('**Latvijas Kendo federācija** uzaicina **visus**, kuri interesējas par Japānas kultūru un kaujas mākslām, kā arī tos, kuri vēlas stiprināt savu veselību, uzlabot fizisko formu, attīstīt izturību, pārliecību par sevi, koordināciju, pilnveidot raksturu un paškontroli, izkopt samuraja cīņas garu, paaugstināt pašnovērtējumu un intelektuālo spēku pievienojieties mums un apgūt Japānas kultūru, kaujas mākslas un pašu Japānu kopā!', icon="ℹ️")
    st.divider()

    st.header('Par federāciju')
    st.image('images/image_1.jpg')
    st.markdown('Kopš dibināšanas brīža mēs sekojam mūsu mērķim – attīstīt Rīgas un Latvijas iedzīvotājos izpratni par Kendo (Japānas paukošanas mākslu), apvienojot fiziskos treniņus ar Japānas kultūrai un vēsturei veltītajām nodarbībām un dodot iespēju mūsdienu jaunatnei un Latvijas iedzīvotājiem attīstīt savas fiziskās un garīgās spējas.')
    st.image('images/image_2.jpg')
    st.divider()

    st.header('Piedavātie sporta veidi')

    st.subheader('Kendo')
    st.image('images/kendo.png')
    st.markdown('**Kendo** – paukošanas māksla, kuras pirmsākumi meklējami tradicionālajā samuraju zobena cīņas tehnikā. Kā mērķis tiek izvirzīts pilnvērtīgas personības un stingrai rakstura veidošana, norūdot paukotāja miesu un garu. Vārdā “zobens” slēpjas Kendo pamatidejas. Cilvēkam, kurš bruņots ar zobenu, nav tiesības kļūdīties un viņam netiks dota iespēja šo kļūdu labot. Tāpēc dzīvē, tāpat kā cīņā, pret visu ir jāizturas nopietni. Kendo katanas vietā tiek izmantots treniņa zobens *šinajs*, ko veido kopā sasietas četras bambusa strēmeles. Tādejādi savainojuma risks tiek samazināts līdz minimumam. Kendo nenozīmē tikai un vienīgi zobena pārvaldības tehniku, kas balstīta uz Visjapānas Kendo federācijas noteikumiem. Ir notikusi pāreja no mākslas iznīcināt ienaidnieku kaujas laukā uz cīnītāja gara ieaudzināšanas mākslu. Kendo tiecas uz enerģiska gara ieaudzināšanu, izmantojot pareizu apmācību un treniņus. Uz cilvēciskās dabas attīstību, balstoties uz darba ar zobenu principu izpratni.')
    st.image('images/kendo_2.png')
    st.divider()

    st.subheader('Iaido')
    st.image('images/iaido_1.jpg')
    st.markdown('**Iaido** – māksla strauji izvilkt zobenu no maksts ar sekojošu uzbrukumu vai pretuzbrukumu pretiniekam, ātra tā neitralizācija ar sekojošu zobena atgriešanu makstī. *Iajdoka* (praktizējošs ar *katanu*) pirmkārt cenšas kontrolēt jau sevi nevis savu pretinieku. Iajdo māksla sastāv no iedomātas cīņas (vadza) apgūšanas un tās izpildes bez reāla partnera klātbūtnes. Iaido sastāv no četrām galvenajām sastāvdaļām: gludām, kontrolētām kustībām , izvelkot zobenu no tā skausta (vai *saya* ), trāpot vai sagriežot pretinieku, noņemot asinis no asmeņa un pēc tam ieliekot zobenu makstī.')
    st.image('images/iaido_2.jpg')
    st.divider()

    st.subheader('Kyudo')
    st.image('images/kyudo.png')
    st.markdown('**Kyudo** - japāņu loka šaušanas māksla. Šis ir viens no tiem retajiem sporta veidiem, nodarbības ar kuru nav atkarīgas nedz no vecuma, nedz dzimuma. Ar Kjudo var nodarboties kā ar mākslu vai meditācijas veidu, taču lielākais vairums nodarbojas ar to kā ar sportu, trenējot pareizu tehnikas izpildi ar mērķi izpildīt skaistu un precīzu šāvienu. Galvenais Kjudo princips ir seijsa seitju (pareizs šāviens, precīzi mērķī), kas nozīmē, ka ievērojot nobiai (loka uzvilkšanas process), šāviens notiek maksimāli dabiski, kas noved pie trāpijuma mērķī. Atbilstoši tam daudzi *kjudokas* (pa Loka Ceļu ejošie) tic sacensību, eksāmenu un visa, kas ļauj pilnveidot šaušanas tehniku, svarīgumam.')
    st.divider()

    st.markdown('Visas šīs disciplīnas glabā Uzlecošās Saules Zemes karavīru filozofiju un senās tradīcijas. Mēs attīstam Latvijā ne tikai kaujas mākslas, bet pievēršam arī uzmanību Japānas kultūrai kopumā. Katru gadu tiek rīkoti semināri un meistarklases tādās disciplīnās kā kaligrāfija Šodo; ziedu kārtošanas māksla Ikebana; tējas ceremonija u.c. Tās vadīt ierodas visaugstākās klases speciālisti no Japānas. Federācijas biedriem ir iespēja apmaiņas programmu ietvaros doties vizītēs uz Japānu. Viena no šādām iespējām ir Kendo sporta delegāciju apmaiņas programmas ietvaros starp sadraudzības pilsētām Rīgu un Kobi.')
    st.image('images/image_3.jpg')
    st.image('images/image_4.jpg')
    st.divider()

    st.image('images/footer.jpg')



if __name__ == '__main__':
    main()
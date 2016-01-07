import xmlclass
'''
sample xml data
<Candidate xmlns="http://ns.hr-xml.org/2007-04-15" xml:lang="en-GB">
<CandidateProfile><ProfileName>Automatically generated Europass CV and xslt from EIfEL</ProfileName>
<PersonalData><PersonDescriptors><DemographicDescriptors><Nationality>French</Nationality>
<PrimaryLanguage>fr</PrimaryLanguage>
</DemographicDescriptors>
<BiologicalDescriptors><DateOfBirth>1972-07-22</DateOfBirth>
<GenderCode>1</GenderCode>
</BiologicalDescriptors>
</PersonDescriptors>
</PersonalData>
</CandidateProfile>
</Candidate>

Stored format:
Candidate
Attributes: xmlns="http://ns.hr-xml.org/2007-04-15" xml:lang="en-GB"
    - CandidateProfile
        - ProfileName
            Data: Automatically generated Europass CV and xslt from EIfEL
        - PersonalData
            - PersonDescriptors
                - DemographicDescriptors
                    - Nationality
                        Data: French
                    - PrimaryLanguage
                        Data: fr
                - BiologicalDescriptors
                    - DateOfBirth
                        Data: 1972-07-22
                    - GenderCode
                        Data: 1
'''
biodes1 = xmlclass.Xmldata('DateOfBirth','1972-07-22')
biodes2 = xmlclass.Xmldata('GenderCode','1')
bio = xmlclass.Xmldata('BiologicalDescriptors')
bio.addele(biodes1)
bio.addele(biodes2)
a = xmlclass.Xmldata('Nationality','French')
b = xmlclass.Xmldata('PrimaryLanguage','fr')
dem = xmlclass.Xmldata('DemographicDescriptors')
dem.addele(a)
dem.addele(b)
per = xmlclass.Xmldata('PersonDescriptors')
per.addele(dem)
per.addele(bio)
p = xmlclass.Xmldata('PersonalData')
p.addele(per)
a = xmlclass.Xmldata('ProfileName','Automatically generated Europass CV and xslt from EIfEL')
b = xmlclass.Xmldata('CandidateProfile')
b.addele(a)
b.addele(p)
root = xmlclass.Xmldata('Candidate')
root.addele(b)
root.addatt('xmlns',"http://ns.hr-xml.org/2007-04-15")
root.addatt('xml:lang',"en-GB")

def simplepass(a):
    print a.name
    if a.have_attributes():
        print 'Attributes : '
        for i in a.atts:
            print i[0],"=",'"',i[1],'"'
    print "\n"
    if a.isdata():
        print "Data: ",a.data
    if a.have_elements():
        for i in a.elements:
            simplepass(i)
    print "\n"

# UK postal code validations

The following python package is designed to validate UK postal codes, as documented in https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom

## Available functions

- validationArea
- validationDistrict
- validationSector
- validationUnit
- validationOutwardCode
- validationInwardCode
- validationUKPostalCode

## Notes for further improvement

- There are some further edge cases in regards to `third` and `fourth` positions in the district codes, that were slightly unclear, and would need further adjusting.
- Test cases dont cover all edge cases, instead the basic A & 9 structure within the wiki's examples.

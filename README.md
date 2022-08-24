# slovom

- Converts decimal currency numbers into words in Bulgarian language
- А single python function with no dependancies which takes a float as an input and converts it into words in Bulgarian.
- Currently works for numbers < 1 000 000.



To do:
- [ ] Add support for other currencies
- [ ] Add support for larger numbers
- [ ] Add support for counting

Example:
```

>>> slovom(1)
'един лев'

>>> slovom(1.50)
'един лев и петдесет стотинки'

>>> slovom(21.50)
'двадесет и eдин лева и петдесет стотинки'

>>> slovom(12345.78)
'дванадесет хиляди триста четиридесет и пет лева и седемдесет и осем стотинки'
```

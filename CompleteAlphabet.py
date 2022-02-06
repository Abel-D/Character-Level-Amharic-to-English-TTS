import pyttsx3

name_for_characters = {
    'ሀ':'haa',
    'ሁ':'hoow',
    'ሂ':'he',
    'ሃ':'haa',
    'ሄ':'hey',
    'ህ':'hee',
    'ሆ':'hoe',
    'ለ':'lae',
    'ሉ':'lu',
    'ሊ':'lee',
    'ላ':'la',
    'ሌ':'lie',
    'ል':'lieh',
    'ሎ':'low',
    'ሐ':'haa',
    'ሑ':'huu',
    'ሒ':'he',
    'ሓ':'haa',
    'ሔ':'hey',
    'ሕ':'hee',
    'ሖ':'hoe',
    'መ':'may',
    'ሙ':'moo',
    'ሚ':'me',
    'ማ':'ma',
    'ሜ':'may',
    'ም':'mee',
    'ሞ':'mow',
    'ሠ':'saah',
    'ሡ':'soo',
    'ሢ':'see',
    'ሣ':'saah',
    'ሤ':'say',
    'ሥ':'see',
    'ሦ':'sow',
    'ረ':'ree',
    'ሩ':'ru',
    'ሪ':'ri',
    'ራ':'ra',
    'ሬ':'rie',
    'ር':'reeee',
    'ሮ':'ro',
    'ሰ':'sye',
    'ሱ':'su',
    'ሲ':'see',
    'ሳ':'sah',
    'ሴ':'say',
    'ስ':'see',
    'ሶ':'so',
    'ሸ':'sheu',
    'ሹ':'shoo',
    'ሺ':'shi',
    'ሻ':'sha',
    'ሼ':'shay',
    'ሽ':'she',
    'ሾ':'sho',
    'ቀ':'ke',
    'ቁ':'ku',
    'ቂ':'key',
    'ቃ':'ka',
    'ቄ':'kay',
    'ቅ':'kea',
    'ቆ':'ko',
    'በ':'baa',
    'ቡ':'bu',
    'ቢ':'bi',
    'ባ':'ba',
    'ቤ':'bay',
    'ብ':'bea',
    'ቦ':'bow',
    'ተ':'tae',
    'ቱ':'tu',
    'ቲ':'tea',
    'ታ':'ta',
    'ቴ':'tey',
    'ት':'tae',
    'ቶ':'tow',
    'ቸ':'che',
    'ቹ':'chu',
    'ቺ':'chi',
    'ቻ':'cha',
    'ቼ':'chey',
    'ች':'chee',
    'ቾ':'cho',
    'ነ':'nay',
    'ኑ':'noo',
    'ኒ':'knee',
    'ና':'na',
    'ኔ':'nay',
    'ን':'nee',
    'ኖ':'no',
    'ኘ':'gnae',
    'ኙ':'gnuw',
    'ኚ':'gnee',
    'ኛ':'gnaa',
    'ኜ':'gnay',
    'ኝ':'gnee',
    'ኞ':'gnow',
    'ደ':'dew',
    'ዱ':'do',
    'ዳ':'dey',
    'ዴ':'day',
    'ድ':'dee',
    'ዶ':'dow',
    'ጀ':'jew',
    'ጁ':'ju',
    'ጂ':'jee',
    'ጃ':'jah',
    'ጄ':'j',
    'ጅ':'jee',
    'ጆ':'jo',
    'ፐ':'paa',
    'ፑ':'pu',
    'ፒ':'pee',
    'ፓ':'pa',
    'ፔ':'pay',
    'ፕ':'pee',
    'ፖ':'pow',
    'ኅ':'haa',
    'ኁ':'hoo',
    'ኂ':'he',
    'ኃ':'haa',
    'ኄ':'hay',
    'ኅ':'hee',
    'ኆ':'how',
}

def say(alphabets):
      return name_for_characters[alphabets]


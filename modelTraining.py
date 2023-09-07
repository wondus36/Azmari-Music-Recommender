{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "50ac34ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8d218487",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"spotify_millsongdata.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "79919672",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Ahe's My Kind Of Girl</td>\n",
       "      <td>/a/abba/ahes+my+kind+of+girl_20598417.html</td>\n",
       "      <td>Look at her face, it's a wonderful face  \\r\\nA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Andante, Andante</td>\n",
       "      <td>/a/abba/andante+andante_20002708.html</td>\n",
       "      <td>Take it easy with me, please  \\r\\nTouch me gen...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>As Good As New</td>\n",
       "      <td>/a/abba/as+good+as+new_20003033.html</td>\n",
       "      <td>I'll never know why I had to go  \\r\\nWhy I had...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Bang</td>\n",
       "      <td>/a/abba/bang_20598415.html</td>\n",
       "      <td>Making somebody happy is a question of give an...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  artist                   song                                        link  \\\n",
       "0   ABBA  Ahe's My Kind Of Girl  /a/abba/ahes+my+kind+of+girl_20598417.html   \n",
       "1   ABBA       Andante, Andante       /a/abba/andante+andante_20002708.html   \n",
       "2   ABBA         As Good As New        /a/abba/as+good+as+new_20003033.html   \n",
       "3   ABBA                   Bang                  /a/abba/bang_20598415.html   \n",
       "\n",
       "                                                text  \n",
       "0  Look at her face, it's a wonderful face  \\r\\nA...  \n",
       "1  Take it easy with me, please  \\r\\nTouch me gen...  \n",
       "2  I'll never know why I had to go  \\r\\nWhy I had...  \n",
       "3  Making somebody happy is a question of give an...  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b61c723f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>57645</th>\n",
       "      <td>Ziggy Marley</td>\n",
       "      <td>Good Old Days</td>\n",
       "      <td>/z/ziggy+marley/good+old+days_10198588.html</td>\n",
       "      <td>Irie days come on play  \\r\\nLet the angels fly...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57646</th>\n",
       "      <td>Ziggy Marley</td>\n",
       "      <td>Hand To Mouth</td>\n",
       "      <td>/z/ziggy+marley/hand+to+mouth_20531167.html</td>\n",
       "      <td>Power to the workers  \\r\\nMore power  \\r\\nPowe...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57647</th>\n",
       "      <td>Zwan</td>\n",
       "      <td>Come With Me</td>\n",
       "      <td>/z/zwan/come+with+me_20148981.html</td>\n",
       "      <td>all you need  \\r\\nis something i'll believe  \\...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57648</th>\n",
       "      <td>Zwan</td>\n",
       "      <td>Desire</td>\n",
       "      <td>/z/zwan/desire_20148986.html</td>\n",
       "      <td>northern star  \\r\\nam i frightened  \\r\\nwhere ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>57649</th>\n",
       "      <td>Zwan</td>\n",
       "      <td>Heartsong</td>\n",
       "      <td>/z/zwan/heartsong_20148991.html</td>\n",
       "      <td>come in  \\r\\nmake yourself at home  \\r\\ni'm a ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             artist           song  \\\n",
       "57645  Ziggy Marley  Good Old Days   \n",
       "57646  Ziggy Marley  Hand To Mouth   \n",
       "57647          Zwan   Come With Me   \n",
       "57648          Zwan         Desire   \n",
       "57649          Zwan      Heartsong   \n",
       "\n",
       "                                              link  \\\n",
       "57645  /z/ziggy+marley/good+old+days_10198588.html   \n",
       "57646  /z/ziggy+marley/hand+to+mouth_20531167.html   \n",
       "57647           /z/zwan/come+with+me_20148981.html   \n",
       "57648                 /z/zwan/desire_20148986.html   \n",
       "57649              /z/zwan/heartsong_20148991.html   \n",
       "\n",
       "                                                    text  \n",
       "57645  Irie days come on play  \\r\\nLet the angels fly...  \n",
       "57646  Power to the workers  \\r\\nMore power  \\r\\nPowe...  \n",
       "57647  all you need  \\r\\nis something i'll believe  \\...  \n",
       "57648  northern star  \\r\\nam i frightened  \\r\\nwhere ...  \n",
       "57649  come in  \\r\\nmake yourself at home  \\r\\ni'm a ...  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d7d8fa2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(57650, 4)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a8fdecf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "artist    0\n",
       "song      0\n",
       "link      0\n",
       "text      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cf5ff69f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Ahe's My Kind Of Girl</td>\n",
       "      <td>/a/abba/ahes+my+kind+of+girl_20598417.html</td>\n",
       "      <td>Look at her face, it's a wonderful face  \\r\\nA...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Andante, Andante</td>\n",
       "      <td>/a/abba/andante+andante_20002708.html</td>\n",
       "      <td>Take it easy with me, please  \\r\\nTouch me gen...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>As Good As New</td>\n",
       "      <td>/a/abba/as+good+as+new_20003033.html</td>\n",
       "      <td>I'll never know why I had to go  \\r\\nWhy I had...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Bang</td>\n",
       "      <td>/a/abba/bang_20598415.html</td>\n",
       "      <td>Making somebody happy is a question of give an...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Bang-A-Boomerang</td>\n",
       "      <td>/a/abba/bang+a+boomerang_20002668.html</td>\n",
       "      <td>Making somebody happy is a question of give an...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Burning My Bridges</td>\n",
       "      <td>/a/abba/burning+my+bridges_20003011.html</td>\n",
       "      <td>Well, you hoot and you holler and you make me ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Cassandra</td>\n",
       "      <td>/a/abba/cassandra_20002811.html</td>\n",
       "      <td>Down in the street they're all singing and sho...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Chiquitita</td>\n",
       "      <td>/a/abba/chiquitita_20002978.html</td>\n",
       "      <td>Chiquitita, tell me what's wrong  \\r\\nYou're e...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Crazy World</td>\n",
       "      <td>/a/abba/crazy+world_20003013.html</td>\n",
       "      <td>I was out with the morning sun  \\r\\nCouldn't s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Crying Over You</td>\n",
       "      <td>/a/abba/crying+over+you_20177611.html</td>\n",
       "      <td>I'm waitin' for you baby  \\r\\nI'm sitting all ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  artist                   song                                        link  \\\n",
       "0   ABBA  Ahe's My Kind Of Girl  /a/abba/ahes+my+kind+of+girl_20598417.html   \n",
       "1   ABBA       Andante, Andante       /a/abba/andante+andante_20002708.html   \n",
       "2   ABBA         As Good As New        /a/abba/as+good+as+new_20003033.html   \n",
       "3   ABBA                   Bang                  /a/abba/bang_20598415.html   \n",
       "4   ABBA       Bang-A-Boomerang      /a/abba/bang+a+boomerang_20002668.html   \n",
       "5   ABBA     Burning My Bridges    /a/abba/burning+my+bridges_20003011.html   \n",
       "6   ABBA              Cassandra             /a/abba/cassandra_20002811.html   \n",
       "7   ABBA             Chiquitita            /a/abba/chiquitita_20002978.html   \n",
       "8   ABBA            Crazy World           /a/abba/crazy+world_20003013.html   \n",
       "9   ABBA        Crying Over You       /a/abba/crying+over+you_20177611.html   \n",
       "\n",
       "                                                text  \n",
       "0  Look at her face, it's a wonderful face  \\r\\nA...  \n",
       "1  Take it easy with me, please  \\r\\nTouch me gen...  \n",
       "2  I'll never know why I had to go  \\r\\nWhy I had...  \n",
       "3  Making somebody happy is a question of give an...  \n",
       "4  Making somebody happy is a question of give an...  \n",
       "5  Well, you hoot and you holler and you make me ...  \n",
       "6  Down in the street they're all singing and sho...  \n",
       "7  Chiquitita, tell me what's wrong  \\r\\nYou're e...  \n",
       "8  I was out with the morning sun  \\r\\nCouldn't s...  \n",
       "9  I'm waitin' for you baby  \\r\\nI'm sitting all ...  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "26eb5b1c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Look at her face, it's a wonderful face  \\r\\nAnd it means something special to me  \\r\\nLook at the way that she smiles when she sees me  \\r\\nHow lucky can one fellow be?  \\r\\n  \\r\\nShe's just my kind of girl, she makes me feel fine  \\r\\nWho could ever believe that she could be mine?  \\r\\nShe's just my kind of girl, without her I'm blue  \\r\\nAnd if she ever leaves me what could I do, what could I do?  \\r\\n  \\r\\nAnd when we go for a walk in the park  \\r\\nAnd she holds me and squeezes my hand  \\r\\nWe'll go on walking for hours and talking  \\r\\nAbout all the things that we plan  \\r\\n  \\r\\nShe's just my kind of girl, she makes me feel fine  \\r\\nWho could ever believe that she could be mine?  \\r\\nShe's just my kind of girl, without her I'm blue  \\r\\nAnd if she ever leaves me what could I do, what could I do?\\r\\n\\r\\n\""
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['text'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "dc76d0f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.sample(5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4a0c4186",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5000, 4)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "865afecc",
   "metadata": {},
   "source": [
    "Text Cleaning/ Text Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b2359525",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['text'] = df['text'].str.lower().replace(r'^\\w\\s', ' ').replace(r'\\n', ' ', regex = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fc679645",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>29268</th>\n",
       "      <td>Deep Purple</td>\n",
       "      <td>Smoke On The Water</td>\n",
       "      <td>/d/deep+purple/smoke+on+the+water_20038742.html</td>\n",
       "      <td>we all came out to montreux  \\r on the lake ge...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37229</th>\n",
       "      <td>Irving Berlin</td>\n",
       "      <td>I'll Share It All With You</td>\n",
       "      <td>/i/irving+berlin/ill+share+it+all+with+you_202...</td>\n",
       "      <td>tommy:]  \\r what is mine, dear, will be yours ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18659</th>\n",
       "      <td>Squeeze</td>\n",
       "      <td>Little King</td>\n",
       "      <td>/s/squeeze/little+king_20129125.html</td>\n",
       "      <td>when the little king  \\r rode on his horse  \\r...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52161</th>\n",
       "      <td>Steely Dan</td>\n",
       "      <td>Hey Nineteen</td>\n",
       "      <td>/s/steely+dan/hey+nineteen_20130113.html</td>\n",
       "      <td>way back when in sixty-seven  \\r i was the dan...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37641</th>\n",
       "      <td>Jennifer Lopez</td>\n",
       "      <td>Hold It Don't Drop It</td>\n",
       "      <td>/j/jennifer+lopez/hold+it+dont+drop+it_2065074...</td>\n",
       "      <td>[chorus]  \\r you don't know what your doin'  \\...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               artist                        song  \\\n",
       "29268     Deep Purple          Smoke On The Water   \n",
       "37229   Irving Berlin  I'll Share It All With You   \n",
       "18659         Squeeze                 Little King   \n",
       "52161      Steely Dan                Hey Nineteen   \n",
       "37641  Jennifer Lopez       Hold It Don't Drop It   \n",
       "\n",
       "                                                    link  \\\n",
       "29268    /d/deep+purple/smoke+on+the+water_20038742.html   \n",
       "37229  /i/irving+berlin/ill+share+it+all+with+you_202...   \n",
       "18659               /s/squeeze/little+king_20129125.html   \n",
       "52161           /s/steely+dan/hey+nineteen_20130113.html   \n",
       "37641  /j/jennifer+lopez/hold+it+dont+drop+it_2065074...   \n",
       "\n",
       "                                                    text  \n",
       "29268  we all came out to montreux  \\r on the lake ge...  \n",
       "37229  tommy:]  \\r what is mine, dear, will be yours ...  \n",
       "18659  when the little king  \\r rode on his horse  \\r...  \n",
       "52161  way back when in sixty-seven  \\r i was the dan...  \n",
       "37641  [chorus]  \\r you don't know what your doin'  \\...  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ffd1bec1",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\wondi\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Unzipping tokenizers\\punkt.zip.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import nltk\n",
    "nltk.download('punkt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7e78451e",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "stemmer = PorterStemmer()\n",
    "\n",
    "def tokenization(txt):\n",
    "    tokens = nltk.word_tokenize(txt)\n",
    "    stemming = [stemmer.stem(w) for w in tokens]\n",
    "    return \" \".join(stemming)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f5c1ece2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df['text'] = df['text'].apply(lambda x: tokenization(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "95fc3be2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f4945e8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "tfidvector = TfidfVectorizer(analyzer='word',stop_words='english')\n",
    "matrix = tfidvector.fit_transform(df['text'])\n",
    "similarity = cosine_similarity(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c1794772",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.        , 0.01360542, 0.02351686, ..., 0.01752148, 0.0053438 ,\n",
       "       0.0331535 ])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "similarity[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "a6221770",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>artist</th>\n",
       "      <th>song</th>\n",
       "      <th>link</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ABBA</td>\n",
       "      <td>Crying Over You</td>\n",
       "      <td>/a/abba/crying+over+you_20177611.html</td>\n",
       "      <td>i 'm waitin ' for you babi i 'm sit all alon i...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  artist             song                                   link  \\\n",
       "9   ABBA  Crying Over You  /a/abba/crying+over+you_20177611.html   \n",
       "\n",
       "                                                text  \n",
       "9  i 'm waitin ' for you babi i 'm sit all alon i...  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['song'] == 'Crying Over You']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5aaa2361",
   "metadata": {},
   "outputs": [],
   "source": [
    "def recommendation(song_df):\n",
    "    idx = df[df['song'] == song_df].index[0]\n",
    "    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])\n",
    "    \n",
    "    songs = []\n",
    "    for m_id in distances[1:21]:\n",
    "        songs.append(df.iloc[m_id[0]].song)\n",
    "        \n",
    "    return songs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "216c25bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cryin Shame',\n",
       " \"Don't Come Cryin' To Me\",\n",
       " 'Vagabond Of The Western World',\n",
       " 'The Storm Is Over Now',\n",
       " 'Here I Am, Send Me',\n",
       " 'Come In From The Outside',\n",
       " \"The End Of The Lyin'\",\n",
       " 'He Was A Friend Of Mine',\n",
       " 'Blue Morning, Blue Day',\n",
       " 'Midnight Blue',\n",
       " 'Deeper',\n",
       " \"For Lovin' Me\",\n",
       " \"Lord Don't Forsake Me\",\n",
       " \"I Don't Want You On My Mind\",\n",
       " 'Strength Of My Life',\n",
       " 'Born To Sing The Blues',\n",
       " 'If I Died Today',\n",
       " 'Baby Blue',\n",
       " \"Baby's Callin' Me Home\",\n",
       " 'Birds Of Paradise']"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recommendation('Crying Over You')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "18192437",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "pickle.dump(similarity,open('similarity.pkl','wb'))\n",
    "pickle.dump(df,open('df.pkl','wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "611029ec",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

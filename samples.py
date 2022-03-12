{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "df988586",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "class pesr:\n",
    "    def __init__(self, data,n):\n",
    "        self.data = data\n",
    "        self.n = n\n",
    "\n",
    "    \n",
    "    def ech_poss(self):\n",
    "        import random\n",
    "        import scipy.special                         ## fonction qui retourne les echantillons possibles vu le mode de prélévement.\n",
    "        k= scipy.special.binom(len(self.data),self.n).astype(int)\n",
    "        c=1\n",
    "        L = [i for i in range(len(self.data))]\n",
    "        z = random.sample(L, self.n)\n",
    "        R = [set(z)]\n",
    "        while c<k:\n",
    "            z = random.sample(L, self.n)\n",
    "            if set(z) in R:\n",
    "                pass\n",
    "            else:\n",
    "                R.append(set(z))\n",
    "                c+=1\n",
    "        return R\n",
    "    \n",
    "    def samples_as(self):\n",
    "        import pandas as pd\n",
    "        import numpy as np\n",
    "        import scipy.special\n",
    "        k = scipy.special.binom(len(self.data), self.n)\n",
    "        k = k.astype(int)\n",
    "        obj = [[] for i in range(k)]                      ### Création des DataFrames des différents échantillons possibles.\n",
    "        dfs = [pd.DataFrame() for i in range(k)]\n",
    "        for i,x in enumerate(self.ech_poss()):\n",
    "            for y in x:\n",
    "                obj[i].append(self.data[y])\n",
    "                dfs[i] = pd.Series(np.array(obj[i])).to_frame()\n",
    "                c = f\"echantillion {i+1}\"\n",
    "                dfs[i].columns = [c]\n",
    "        horizontal_concat = pd.concat([dfs[i] for i in range(k)], axis=1)\n",
    "        print('Les échantillons possibles à prélever vu le mode de prélevement (probabilités égales sans remise) sont présentés\\n dans le tableau ci-dessous: ')\n",
    "        return horizontal_concat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "0c58bdb3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{2, 3}, {1, 2}, {0, 1}, {1, 3}, {0, 2}, {0, 3}]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pesr([2,2,1,4], 2).ech_poss()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c753481b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Les échantillons possibles à prélever vu le mode de prélevement (probabilités égales sans remise) sont présentés\n",
      " dans le tableau ci-dessous: \n"
     ]
    },
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
       "      <th>echantillion 1</th>\n",
       "      <th>echantillion 2</th>\n",
       "      <th>echantillion 3</th>\n",
       "      <th>echantillion 4</th>\n",
       "      <th>echantillion 5</th>\n",
       "      <th>echantillion 6</th>\n",
       "      <th>echantillion 7</th>\n",
       "      <th>echantillion 8</th>\n",
       "      <th>echantillion 9</th>\n",
       "      <th>echantillion 10</th>\n",
       "      <th>echantillion 11</th>\n",
       "      <th>echantillion 12</th>\n",
       "      <th>echantillion 13</th>\n",
       "      <th>echantillion 14</th>\n",
       "      <th>echantillion 15</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   echantillion 1  echantillion 2  echantillion 3  echantillion 4  \\\n",
       "0               4               4               1               3   \n",
       "1               5               6               4               4   \n",
       "\n",
       "   echantillion 5  echantillion 6  echantillion 7  echantillion 8  \\\n",
       "0               1               5               1               1   \n",
       "1               2               6               3               6   \n",
       "\n",
       "   echantillion 9  echantillion 10  echantillion 11  echantillion 12  \\\n",
       "0               2                2                2                3   \n",
       "1               6                5                4                5   \n",
       "\n",
       "   echantillion 13  echantillion 14  echantillion 15  \n",
       "0                3                1                2  \n",
       "1                6                5                3  "
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pesr([1,2,3,4,5,6], 2).samples_as()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bccb30dd",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

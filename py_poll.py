{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3ce91ec3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "085a799a",
   "metadata": {},
   "outputs": [],
   "source": [
    "file_to_load = 'Resources.csv/election_results.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "eef7ce52",
   "metadata": {},
   "outputs": [],
   "source": [
    "election_data = pd.read_csv(file_to_load)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0051a060",
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
       "      <th>Ballot ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1323913</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1005842</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1880345</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1600337</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1835994</td>\n",
       "      <td>Jefferson</td>\n",
       "      <td>Charles Casper Stockham</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Ballot ID     County                Candidate\n",
       "0    1323913  Jefferson  Charles Casper Stockham\n",
       "1    1005842  Jefferson  Charles Casper Stockham\n",
       "2    1880345  Jefferson  Charles Casper Stockham\n",
       "3    1600337  Jefferson  Charles Casper Stockham\n",
       "4    1835994  Jefferson  Charles Casper Stockham"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "election_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50647d02",
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

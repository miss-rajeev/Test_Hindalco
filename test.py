{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from pandas_profiling import ProfileReport"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_excel(r\"C:\\Users\\aishwarya.r\\OneDrive - Aditya Birla Group\\Documents\\Work_101\\KILN_Hindalco\\Raw Data-Copy1.xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import load_diabetes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "diab_data=load_diabetes()\n",
    "df=pd.DataFrame(data=diab_data.data,columns=diab_data.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>bp</th>\n",
       "      <th>s1</th>\n",
       "      <th>s2</th>\n",
       "      <th>s3</th>\n",
       "      <th>s4</th>\n",
       "      <th>s5</th>\n",
       "      <th>s6</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.038076</td>\n",
       "      <td>0.050680</td>\n",
       "      <td>0.061696</td>\n",
       "      <td>0.021872</td>\n",
       "      <td>-0.044223</td>\n",
       "      <td>-0.034821</td>\n",
       "      <td>-0.043401</td>\n",
       "      <td>-0.002592</td>\n",
       "      <td>0.019908</td>\n",
       "      <td>-0.017646</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.001882</td>\n",
       "      <td>-0.044642</td>\n",
       "      <td>-0.051474</td>\n",
       "      <td>-0.026328</td>\n",
       "      <td>-0.008449</td>\n",
       "      <td>-0.019163</td>\n",
       "      <td>0.074412</td>\n",
       "      <td>-0.039493</td>\n",
       "      <td>-0.068330</td>\n",
       "      <td>-0.092204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.085299</td>\n",
       "      <td>0.050680</td>\n",
       "      <td>0.044451</td>\n",
       "      <td>-0.005671</td>\n",
       "      <td>-0.045599</td>\n",
       "      <td>-0.034194</td>\n",
       "      <td>-0.032356</td>\n",
       "      <td>-0.002592</td>\n",
       "      <td>0.002864</td>\n",
       "      <td>-0.025930</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-0.089063</td>\n",
       "      <td>-0.044642</td>\n",
       "      <td>-0.011595</td>\n",
       "      <td>-0.036656</td>\n",
       "      <td>0.012191</td>\n",
       "      <td>0.024991</td>\n",
       "      <td>-0.036038</td>\n",
       "      <td>0.034309</td>\n",
       "      <td>0.022692</td>\n",
       "      <td>-0.009362</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.005383</td>\n",
       "      <td>-0.044642</td>\n",
       "      <td>-0.036385</td>\n",
       "      <td>0.021872</td>\n",
       "      <td>0.003935</td>\n",
       "      <td>0.015596</td>\n",
       "      <td>0.008142</td>\n",
       "      <td>-0.002592</td>\n",
       "      <td>-0.031991</td>\n",
       "      <td>-0.046641</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        age       sex       bmi        bp        s1        s2        s3  \\\n",
       "0  0.038076  0.050680  0.061696  0.021872 -0.044223 -0.034821 -0.043401   \n",
       "1 -0.001882 -0.044642 -0.051474 -0.026328 -0.008449 -0.019163  0.074412   \n",
       "2  0.085299  0.050680  0.044451 -0.005671 -0.045599 -0.034194 -0.032356   \n",
       "3 -0.089063 -0.044642 -0.011595 -0.036656  0.012191  0.024991 -0.036038   \n",
       "4  0.005383 -0.044642 -0.036385  0.021872  0.003935  0.015596  0.008142   \n",
       "\n",
       "         s4        s5        s6  \n",
       "0 -0.002592  0.019908 -0.017646  \n",
       "1 -0.039493 -0.068330 -0.092204  \n",
       "2 -0.002592  0.002864 -0.025930  \n",
       "3  0.034309  0.022692 -0.009362  \n",
       "4 -0.002592 -0.031991 -0.046641  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

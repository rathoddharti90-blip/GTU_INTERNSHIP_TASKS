{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ce4c0c8-421f-4a56-949d-d1c36d6e9366",
   "metadata": {},
   "outputs": [],
   "source": [
    "#DATA SCIENCE DAY 5  \n",
    "#ASSESMENT\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5e4a0387-7994-4671-a718-b57a012e327f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter numberb of terms 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci Series:\n",
      "0 1 1 2 3 5 8 13 21 34 "
     ]
    }
   ],
   "source": [
    "#Q1) WRITE A PROGRAM TO FIND FIBONACCI SERIES\n",
    "n=int(input(\"Enter numberb of terms\"))\n",
    "\n",
    "a=0\n",
    "b=1\n",
    "\n",
    "print(\"Fibonacci Series:\")\n",
    "\n",
    "for i in range(n): \n",
    "    print(a,end=\" \")\n",
    "    c=a+b\n",
    "    a=b\n",
    "    b=c\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3092ce67-90f9-47f0-8e61-6f5c3f2d5618",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a string:  madam\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pallindrome\n"
     ]
    }
   ],
   "source": [
    "#Q2) WRITE A PROGRAM TO EVALUATE A STRING WHETHER IT IS PALLINDROME OR NOT\n",
    "\n",
    "s=input(\"Enter a string: \")\n",
    "rev=\"\"\n",
    "for i in s:\n",
    "    rev=i+rev\n",
    "if s==rev:\n",
    "    print(\"Pallindrome\")\n",
    "else:\n",
    "    print(\"Not a Pallindrome\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "25e687b7-9968-438a-8ba2-5ab17c7344b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter fathers income 80000\n",
      "Enter mothers income 50000\n",
      "Enter son's income 40000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total income= 170000.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter House rent:  20000\n",
      "Enter food expense:  3000\n",
      "Enter electricity expense:  2500\n",
      "Enter Transport expense:  2400\n",
      "Enter other expenses:  4300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Expense=  32200.0\n",
      "Net Gross Income=  137800.0\n"
     ]
    }
   ],
   "source": [
    "#Q3) WRITE A PROGRAM TO CALCULATE THE GROSS INCOME OF A FAMILY\n",
    "\n",
    "father=float(input(\"Enter fathers income\"))\n",
    "mother=float(input(\"Enter mothers income\"))\n",
    "son=float(input(\"Enter son's income\"))\n",
    "\n",
    "total=father+mother+son\n",
    "\n",
    "print(\"Total income=\",total)\n",
    "\n",
    "rent=float(input(\"Enter House rent: \"))\n",
    "food=float(input(\"Enter food expense: \"))\n",
    "elec=float(input(\"Enter electricity expense: \"))\n",
    "trps=float(input(\"Enter Transport expense: \"))\n",
    "other=float(input(\"Enter other expenses: \"))\n",
    "\n",
    "totalexp=rent+food+elec+trps+other\n",
    "\n",
    "print(\"Total Expense= \",totalexp)\n",
    "net=total-totalexp\n",
    "\n",
    "print(\"Net Gross Income= \",net)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "18725a68-f5a2-43de-a69e-d686cf06fce0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\t\t\t CALCULATOR\t\t\t\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number 23\n",
      "Enter second number 34\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Choose operation\n",
      "1 Addition\n",
      "2 Subtraction\n",
      "3 Multiplication\n",
      "4 Division\n",
      "5 Percentage\n",
      "6 Power\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice(1-6) 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition= 57.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to continue?(Y/N) y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Choose operation\n",
      "1 Addition\n",
      "2 Subtraction\n",
      "3 Multiplication\n",
      "4 Division\n",
      "5 Percentage\n",
      "6 Power\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice(1-6) 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Subtraction= -11.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to continue?(Y/N) y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Choose operation\n",
      "1 Addition\n",
      "2 Subtraction\n",
      "3 Multiplication\n",
      "4 Division\n",
      "5 Percentage\n",
      "6 Power\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice(1-6) 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Multiplication= 782.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to continue?(Y/N) y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Choose operation\n",
      "1 Addition\n",
      "2 Subtraction\n",
      "3 Multiplication\n",
      "4 Division\n",
      "5 Percentage\n",
      "6 Power\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice(1-6) 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Division= 0.6764705882352942\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to continue?(Y/N) y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Choose operation\n",
      "1 Addition\n",
      "2 Subtraction\n",
      "3 Multiplication\n",
      "4 Division\n",
      "5 Percentage\n",
      "6 Power\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice(1-6) 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Percentage= 147.82608695652175\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to continue?(Y/N) y\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Choose operation\n",
      "1 Addition\n",
      "2 Subtraction\n",
      "3 Multiplication\n",
      "4 Division\n",
      "5 Percentage\n",
      "6 Power\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice(1-6) 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Power= 1.9895113660064588e+46\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to continue?(Y/N) n\n"
     ]
    }
   ],
   "source": [
    "# Q4 To create a basic calculator\n",
    "print(\"\\t\\t\\t CALCULATOR\\t\\t\\t\")\n",
    "a=float(input(\"Enter first number\"))\n",
    "b=float(input(\"Enter second number\"))\n",
    "while True:\n",
    "    \n",
    "\n",
    "    print(\"\\nChoose operation\")\n",
    "    print(\"1 Addition\")\n",
    "    print(\"2 Subtraction\")\n",
    "    print(\"3 Multiplication\")\n",
    "    print(\"4 Division\")\n",
    "    print(\"5 Percentage\")\n",
    "    print(\"6 Power\")\n",
    "\n",
    "    ch=int(input(\"Enter your choice(1-6)\"))\n",
    "    if ch==1:\n",
    "        print(\"Addition=\",a+b)\n",
    "\n",
    "    elif ch==2:\n",
    "        print(\"Subtraction=\",a-b)\n",
    "    elif ch==3:\n",
    "        print(\"Multiplication=\",a*b)\n",
    "    elif ch==4:\n",
    "        print(\"Division=\",a/b)\n",
    "    elif ch==5:\n",
    "        print(\"Percentage=\",(b*100)/a)\n",
    "    elif ch==6:\n",
    "        print(\"Power=\",a ** b)\n",
    "    else:\n",
    "        print(\"Invalid Choice\")\n",
    "    c=input(\"\\nDo you want to continue?(Y/N)\")\n",
    "    if c==\"N\" or c==\"n\":\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4701eb02-ec6e-4771-bfff-047232bfd2c4",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

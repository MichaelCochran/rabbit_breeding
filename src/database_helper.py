import sqlite3

class DatabaseHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Animals (
            AnimalID INT PRIMARY KEY,
            Species VARCHAR(50),
            Age INT,
            HealthStatus VARCHAR(50),
            IdentificationNumber VARCHAR(50),
            ParentID1 INT,
            ParentID2 INT,
            FOREIGN KEY (ParentID1) REFERENCES Animals(AnimalID),
            FOREIGN KEY (ParentID2) REFERENCES Animals(AnimalID))""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS MatingPairs (
            PairID INT PRIMARY KEY,
            MaleAnimalID INT,
            FemaleAnimalID INT,
            MatingDates DATE,
            ConceptionRates FLOAT,
            LitterSize INT,
            BirthRate FLOAT,
            IntervalsBetweenBirths INT,
            StillbirthRate FLOAT,
            BirthWeight FLOAT,
            FOREIGN KEY (MaleAnimalID) REFERENCES Animals(AnimalID),
            FOREIGN KEY (FemaleAnimalID) REFERENCES Animals(AnimalID))""")
    
        self.cur.execute("""CREATE TABLE IF NOT EXISTS GrowthProductivityMetrics (
            AnimalID INT PRIMARY KEY,
            GrowthRate FLOAT,
            FeedConversionRatio FLOAT,
            MilkProductionQuantity FLOAT,
            MilkProductionQuality VARCHAR(50),
            ProductQuality VARCHAR(50),
            LongevityLifespan INT,
            LongevityProductiveYears INT,
            WasteProduction FLOAT,
            FOREIGN KEY (AnimalID) REFERENCES Animals(AnimalID))""")
        
        self.cur.execute("""CREATE TABLE IF NOT EXISTS HealthIndicators (
            HealthID INT PRIMARY KEY,
            AnimalID INT,
            DiseaseOccurrences VARCHAR(255),
            VeterinaryInterventions VARCHAR(255),
            MortalityRates FLOAT,
            FOREIGN KEY (AnimalID) REFERENCES Animals(AnimalID))""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS BehavioralIndicators (
            BehaviorID INT PRIMARY KEY,
            AnimalID INT,
            SignsOfStress VARCHAR(255),
            SignsOfWellBeing VARCHAR(255),
            FOREIGN KEY (AnimalID) REFERENCES Animals(AnimalID))""")
        
        self.cur.execute("""CREATE TABLE IF NOT EXISTS EconomicData (
            EconomicID INT PRIMARY KEY,
            AnimalID INT,
            FeedCosts FLOAT,
            HealthcareCosts FLOAT,
            OverallMaintenanceCosts FLOAT,
            RevenueEarned FLOAT,
            FOREIGN KEY (AnimalID) REFERENCES Animals(AnimalID))""")
    
        # self.cur.execute('''
        #     CREATE TABLE IF NOT EXISTS rabbits (
        #         name TEXT,
        #         last_bred TEXT,
        #         buck TEXT,
        #         palpatate TEXT,
        #         nest_date TEXT,
        #         due_date TEXT,
        #         comments TEXT
        #     )
        # ''')

    def insert_data(self, name, bred, buck, palpitating, nest, due, comments):
        try:
            self.cur.execute("INSERT INTO rabbits VALUES (?, ?, ?, ?, ?, ?, ?)", 
                             (name, bred, buck, palpitating, nest, due, comments))
            self.conn.commit()
            print("\nData added to file")
        except Exception as e:
            print("Error:", e)

    def view_data(self):
        self.cur.execute("SELECT * FROM rabbits")
        return self.cur.fetchall()

    def close_connection(self):
        self.conn.close()
        
    def delete_data(self, name, last_bred):
        try:
            self.cur.execute("DELETE FROM rabbits WHERE name = ? and last_bred = ?", (name, last_bred))
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
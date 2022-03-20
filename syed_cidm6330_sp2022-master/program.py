from bmi.health_record import HealthRecord, HealthRecordFactory

def main():
    hr = HealthRecordFactory.make_health_record(15, 15, "F", 27)
    print(hr)

if __name__ == "__main__":
    main()
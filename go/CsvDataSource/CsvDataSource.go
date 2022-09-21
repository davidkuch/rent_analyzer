package CsvDataSource

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"

	"../DataFormat"
)

func getCsvObj(filename string) [][]string {
	file, err := os.Open(filename)

	defer file.Close()

	if err != nil {
		fmt.Println("err open file")
	}

	csvReader := csv.NewReader(file)

	data, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	return data
}

func cleanCsvObj(obj *[][]string) [][]string {

	var clean [][]string

	for _, row := range *obj {
		if row[0] != "" {
			clean = append(clean, row)
		}
	}

	return clean
}

func parseCsvObj(obj *[][]string) {
	var parsed DataFormat.RentData

}

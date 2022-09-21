package DataFormat

import "time"

type row struct {
	capacity      int
	monthly_price int
	start_day     time.Date
	end_day       time.Date
}

type RentData []row

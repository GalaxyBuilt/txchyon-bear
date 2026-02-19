// src/lib/utils/dateFormat.ts
import { format, parseISO } from "date-fns";

export default function dateFormat(dateInput: string | Date | undefined): string {
  if (!dateInput) return "No date";

  let date: Date;

  if (typeof dateInput === "string") {
    // Handle both "2025-11-24" and "2025-11-24T05:00:00Z"
    date = new Date(dateInput);
  } else {
    date = dateInput;
  }

  if (isNaN(date.getTime())) return "Invalid date";

  return format(date, "dd MMM yyyy"); // → 24 Nov 2025
}
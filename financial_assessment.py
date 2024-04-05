def assess_financial_condition_logic(ratios):
  """
  This function assesses the financial condition based on provided ratios and returns
  a string representing the assessment and a list of recommendations.

  Args:
      ratios: A dictionary containing calculated financial ratios.

  Returns:
      A tuple containing the financial condition (string) and recommendations (list).
  """

  condition = ""
  recommendations = []

  # Extract relevant data from the ratios dictionary
  current_ratio = ratios.get("current_ratio")
  quick_ratio = ratios.get("quick_ratio")
  debt_to_equity_ratio = ratios.get("debt_to_equity_ratio")
  interest_coverage_ratio = ratios.get("interest_coverage_ratio")
  profit_margin_ratio = ratios.get("profit_margin_ratio")
  roa_ratio = ratios.get("roa_ratio")
  roe_ratio = ratios.get("roe_ratio")
  gross_margin_ratio = ratios.get("gross_margin_ratio")
  operating_margin_ratio = ratios.get("operating_margin_ratio")

  # Define thresholds for each ratio (adjust as needed)
  current_ratio_threshold = 1.5
  quick_ratio_threshold = 1.0
  debt_to_equity_threshold = 0.5
  interest_coverage_threshold = 3.0
  profit_margin_threshold = 0.1
  roa_threshold = 0.05
  roe_threshold = 0.15
  gross_margin_threshold = 0.6  # Example threshold for gross margin

  # Assess financial condition based on thresholds
  if (current_ratio >= current_ratio_threshold
      and quick_ratio >= quick_ratio_threshold
      and debt_to_equity_ratio <= debt_to_equity_threshold
      and interest_coverage_ratio >= interest_coverage_threshold
      and profit_margin_ratio >= profit_margin_threshold
      and roa_ratio >= roa_threshold
      and roe_ratio >= roe_threshold
      and gross_margin_ratio >= gross_margin_threshold if gross_margin_ratio else True):  # Consider gross margin if available
    condition = "Good"
    recommendations = [
      "Maintain healthy financial position.",
      "Consider growth opportunities.",
      "Optimize investment strategies."
    ]
  elif (current_ratio >= 1 and quick_ratio >= 0.8
        and debt_to_equity_ratio <= 1
        and interest_coverage_ratio >= 2
        and profit_margin_ratio >= 0.05
        and roa_ratio >= 0.03
        and roe_ratio >= 0.1):
    condition = "Fair"
    recommendations = [
      "Improve liquidity by reducing short-term liabilities.",
      "Increase cash flow and profitability.",
      "Explore opportunities to reduce debt burden."
    ]
  else:
    condition = "Poor"
    recommendations = [
      "Prioritize reducing short-term liabilities.",
      "Increase current assets and liquidity.",
      "Identify ways to improve profitability and efficiency."
      "Analyze the reasons behind low gross margin if available (consider cost management or pricing strategies)."  # Add recommendation if gross margin is low
    ]

  return condition, recommendations


-- Aproximar la integral de f desde a hasta b con n subdivisiones
integral :: (Double -> Double) -> Double -> Double -> Int -> Double
integral f a b n =
  let h = (b - a) / fromIntegral n
      x i = a + fromIntegral i * h
      suma = sum [f (x i) | i <- [1 .. n - 1]]
  in  h / 2 * (f a + 2 * suma + f b)

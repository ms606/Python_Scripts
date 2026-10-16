const PLANETARY_MAP: Record<string,number> = {
    mercury: 0.2408467,
    venus:	0.61519726,
    earth:	1.0,
    mars:	1.8808158,
    jupiter:11.862615,
    saturn:	29.447498,
    uranus:	84.016846,
    neptune:164.79132,
  } as const;

  type Planet = keyof typeof PLANETARY_MAP;

const EARTH_YEAR_IN_SECONDS = 31557600;

export function age(planet: Planet, seconds: number): number {

  const space_age = seconds / (PLANETARY_MAP[planet] * EARTH_YEAR_IN_SECONDS);
  
  return Math.round(space_age * 100) / 100 
}
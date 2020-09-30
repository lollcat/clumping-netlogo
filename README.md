# Plant-Dioecy-Hermaphrodites
Simulating competition between diocious and hermaphroditic plants, in an environment with periodic burning

# Description
 - populate the area with a selected number of hermaphroditic (green) and diocous (males are blue, females are red) plants
    -  Starts with double the number of dioecy than hermaphrodites

**The following is then repeated**

 - **compete**: Only one plant can survive on a patch at a time
    - for patches with more than one plant, a plant on the patch is randomly selected to survive, while the rest die
 - **set-seeds**: Each female dioecy produces a selected number of seeds (by the user, using the slider), each hermaphrodite produces a selected number of seeds
 - **disperse-seeds**: The seeds move a specified (by user) distance from their parent, in a random direction
 - **burn**: The fire comes, all adult plants die
  

# Assumptions
  - no pollination included
    - plants are assumed just to produce a set amount of seeds which become adults

# Simulating plants with Netlogo
## Clumping
Simulating clumping behavior of new seedlings, as a function of dispersal distance / number of seedlings per parent.



## Plant-Dioecy-Hermaphrodites
Simulating competition between diocious and hermaphroditic plants, in an environment with periodic burning.
Using Netlogo

### Simulation Description
**Setup**
 - populate the area with a selected number of hermaphroditic (green) and dioecious (males are blue, females are red) plants

**Go**

**The following set of steps are repeated**

 - **compete**: Only one plant can survive on a patch at a time
    - for patches with more than one plant, a plant on the patch is randomly selected to survive, while the rest die
 - **set-seeds**: Each female dioecy produces a selected number of seeds (by the user, using the slider), each hermaphrodite produces a selected number of seeds
 - **disperse-seeds**: The seeds move a specified (by user) distance from their parent, in a random direction
 - **burn**: The fire comes, all adult plants die
  

### Assumptions
  - no pollination included
    - plants are assumed just to produce a set amount of seeds which become adults
  - dispersal just moves a set amount in a random direction
     - this could be changed to instead move a random amount (according to some probability distribution) in a random direction

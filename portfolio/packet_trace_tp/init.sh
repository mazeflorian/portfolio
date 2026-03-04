
set -e
git init 
touch README.md
echo "Cisco CT" >> README.md
mkdir -p topology-1/diagrams \
    topology-1/switch \
    topology-1/multiplayer-switch \
    topology-1/routers \
    topology-1/hots
touch topology-1/switch/vlan.config \
    topology-1/switch/global.config \
    topology-1/routeurs/router-ent/global.config \
    topology-1/routers/router-ent/subinterfaces.config
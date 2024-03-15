mkdir -p "service-result/"

docker cp "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e:/home/doc-bd-a1/res_dpre.csv" "service-result/"
docker cp "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e:/home/doc-bd-a1/eda-in-1.txt" "service-result/"
docker cp "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e:/home/doc-bd-a1/eda-in-2.txt" "service-result/"
docker cp "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e:/home/doc-bd-a1/eda-in-3.txt" "service-result/"
docker cp "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e:/home/doc-bd-a1/vis.png" "service-result/"
docker cp "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e:/home/doc-bd-a1/k.txt" "service-result/"

docker stop "45cd0c7e98030e111a514b6d344aed179c44fc36fcc6a7ecdc0f655b0fc26e1e"

echo "Output files copied to 'service-result/'"
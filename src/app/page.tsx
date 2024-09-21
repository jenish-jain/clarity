import { Header } from "./components/header";
import { Link } from "@mui/joy";
import Box from "@mui/joy/Box";

export default function Page() {
  let showDrawer = true;
  return (
    <div>
      <Header sticky showDrawer={showDrawer} />
      <Box
        className="poppins-bold"
        sx={{ display: "flex", alignItems: "center", justifyContent: "center" }}
      >
        <div>Click to visualise your expenses</div>
        <Link href="/glasses">
          <img
            src="./magnifying-glass.svg"
            alt="404"
            className="mx-auto mb-7.5"
            width={400}
            height={400}
          />
        </Link>
      </Box>
    </div>
  );
}

import argparse
import datetime
import ipaddress
import sys

def handleDash(ip_data):
    '''
    Parses IP ranges with "-" substring into ipaddress.IPv4Network objects
    Arg 1: IP range string
    '''
    data = ip_data.split("-")
    start_ip = data[0].strip(" ")
    start_ip_ipv4 = ipaddress.IPv4Address(start_ip)

    end_ip_4oct = data[1].strip(" ")
    end_ip_arr = start_ip.split(".")
    end_ip_arr[3] = end_ip_4oct
    end_ip_ipv4 = ipaddress.IPv4Address(".".join(end_ip_arr))
    ranges = [ipaddr for ipaddr in ipaddress.summarize_address_range(start_ip_ipv4, end_ip_ipv4)]

        
    return ranges


def handleCIDR(ip_network_data):
    '''
    Iterates over a ipaddress.ip_network object and prints IP addresses.
    Arg 1: ipaddress.ip_network object
    '''
    ips = [str(ip) for ip in ip_network_data]
    return ips


def main():
    # Local array storage
    allIPs = []
    totalRanges = 0

    # Create command line argument object
    parser = argparse.ArgumentParser(description="Parse CIDRs and IP ranges to single IP addresses", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-r", "--ranges", help="Text file with IP ranges on each line")
    parser.add_argument("-o", "--output", help="Output file name (.txt is appended)", default=str(datetime.datetime.now().timestamp())+"_output.txt")
    parser.add_argument("-v", "--verbose", help="Print more info", action="store_true")

	# Parse and manage arguments
    args = parser.parse_args()

    # -r, --ranges argument
    if args.ranges == None:
        parser.print_help()
        print("")
        print("")
        print("[!] ERROR: -r, --ranges was not specified")
        sys.exit(1)
    else:
        ranges = args.ranges

    # Format output file
    file_output = args.output+".txt"

    # Spacing line
    print("")

    # Read in ranges
    if args.verbose: print("[+] Reading in ranges from: "+ranges)
    with open(ranges) as f:
        lines = [ line.strip() for line in f ]
        totalRanges = len(lines)

    # Loop over all data
    if args.verbose: print("[+] Looping over data")
    for ip_data in lines:
        if args.verbose: print("")

        # Handle "-", " - ", "- ", " -"
        if "-" in ip_data:
            if args.verbose: print("[+] Data '{0}' contains a dash".format(ip_data))
            ranges = handleDash(ip_data)
            for range in ranges:
                if args.verbose: print("  Range found: {0}".format(range))
                for ip in range.hosts():
                    if args.verbose: print("    IP found: {0}".format(ip))
                    allIPs.append(ip)
            
        # Handle cidr
        elif "/" in ip_data:
            if args.verbose: print("[+] Data '{0}' contains a slash".format(ip_data))
            if args.verbose: print("  Range found {0}".format(ip_data))
            ips = handleCIDR(ipaddress.ip_network(ip_data, False))
            for ip in ips:
                if args.verbose: print("    IP found: {0}".format(ip))
                allIPs.append(ip)
        
        else:
            print("")
            print("-------------------")
            print("[!] Not a valid range: {0}".format(ip_data))
            print("-------------------")
            print("")

    # Write out data
    if args.verbose: print("[+] Writing data to output file {0}".format(file_output))
    o = open(file_output, "w")
    for ip in allIPs:
        o.write("{0}\n".format(ip))

    o.close()

    # Print runtime info
    print("=================")
    print("Total ranges: "+str(totalRanges))
    print("Total IPs: "+str(len(allIPs)))
    print("")
    print("Output file: "+file_output)
    print("=================")

# Run main if script
if __name__ == "__main__":
    main()